from http.server import BaseHTTPRequestHandler
from data.redis_client import get_redis_connection
import json


class ResponsesHandler(BaseHTTPRequestHandler):
    """Controlador para manejar /get-responses y /clear-responses, con validación de token."""

    # -------------------------------
    # Utilidades internas
    # -------------------------------
    def _send_json(self, data, status=200):
        """Envia una respuesta JSON con el código de estado dado."""
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _validate_token(self):
        """Valida el token desde Redis usando el header Authorization: Bearer <token>."""
        auth_header = self.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return False

        token = auth_header.split(" ")[1]
        r = get_redis_connection()
        return r.exists(f"token:{token}") == 1

    def log_message(self, format, *args):
        """Evita logs por consola en el servidor."""
        return

    # -------------------------------
    # Endpoints
    # -------------------------------
    def do_GET(self):
        """Devuelve todas las respuestas almacenadas en Redis."""
        if self.path.rstrip("/") == "/get-responses":
            if not self._validate_token():
                self._send_json({"message": "Invalid or missing token"}, status=401)
                return

            r = get_redis_connection()
            data = r.lrange("health_requests", 0, -1)
            responses = [json.loads(item) for item in data]
            self._send_json(responses, status=200)

    def do_DELETE(self):
        """Elimina todas las respuestas almacenadas."""
        if self.path.rstrip("/") == "/clear-responses":
            if not self._validate_token():
                self._send_json({"message": "Invalid or missing token"}, status=401)
                return

            r = get_redis_connection()
            r.delete("health_requests")
            self._send_json({"message": "All responses have been cleared successfully"}, status=200)
