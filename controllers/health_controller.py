from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from data.redis_client import get_redis_connection
import json
import threading
import time


class HealthHandler(BaseHTTPRequestHandler):
    server_version = "RoomBookingHealth/1.0"

    def do_GET(self):  # noqa: N802 (naming by stdlib)
        if self.path.rstrip("/") == "/health":
            payload = {
                "status": "ok",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "client_ip": self.client_address[0],
            }

            r = get_redis_connection()
            r.rpush("health_requests", json.dumps(payload))

            body = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404, "Not Found")

    def log_message(self, format, *args):  # noqa: A003
        return


def start_health_server(host: str = "127.0.0.1", port: int = 8000):
    """Arranca el servidor HTTP en un thread (no bloquea)."""
    httpd = ThreadingHTTPServer((host, port), HealthHandler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd, t


if __name__ == "__main__":
    print("Servidor de health corriendo en http://127.0.0.1:8000/health")
    server, _t = start_health_server(host="0.0.0.0", port=8000)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
        server.shutdown()
        server.server_close()
