import pytest
import threading
import time
import requests
from http.server import HTTPServer
from controllers.health_controller import HealthHandler
from controllers.responses_controller import ResponsesHandler
from data.redis_client import get_redis_connection


class CombinedHandler(HealthHandler, ResponsesHandler):
    """Handler combinado para enrutar /health, /get-responses y /clear-responses."""
    def do_GET(self):
        if self.path.rstrip("/") == "/health":
            HealthHandler.do_GET(self)
        elif self.path.rstrip("/") == "/get-responses":
            ResponsesHandler.do_GET(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_DELETE(self):
        if self.path.rstrip("/") == "/clear-responses":
            ResponsesHandler.do_DELETE(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def log_message(self, format, *args):
        return


@pytest.fixture(scope="module", autouse=True)
def start_server():
    """Levanta el servidor HTTP para pruebas."""
    server = HTTPServer(("localhost", 8000), CombinedHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(1)  # Espera a que el server inicie
    yield
    server.shutdown()


def test_health_endpoint():
    """Verifica que /health devuelva status 200 y contenga 'ok'."""
    response = requests.get("http://localhost:8000/health")
    assert response.status_code == 200
    assert "ok" in response.text


def test_get_responses_requires_token():
    """Verifica que /get-responses sin token devuelva 401."""
    response = requests.get("http://localhost:8000/get-responses")
    assert response.status_code == 401
    assert "Invalid" in response.text


def test_get_responses_with_valid_token():
    """Verifica que /get-responses devuelva 200 con token válido."""
    r = get_redis_connection()
    r.set("token:12345", "valid")
    response = requests.get(
        "http://localhost:8000/get-responses",
        headers={"Authorization": "Bearer 12345"},
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")


def test_clear_responses():
    """Verifica que /clear-responses elimine los datos."""
    r = get_redis_connection()
    r.set("token:12345", "valid")
    r.rpush("health_requests", '{"status": "ok"}')

    response = requests.delete(
        "http://localhost:8000/clear-responses",
        headers={"Authorization": "Bearer 12345"},
    )
    assert response.status_code == 200
    assert "cleared successfully" in response.text

    # Verifica que los datos hayan sido borrados
    assert r.llen("health_requests") == 0
