from http.server import BaseHTTPRequestHandler
from data.redis_client import get_redis_connection
import json


class ResponsesHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.rstrip("/") == "/get-responses":
            # Middleware manual
            if not self.validate_token():
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'{"message": "Invalid or missing token"}')
                return

            r = get_redis_connection()
            data = r.lrange("health_requests", 0, -1)
            responses = [json.loads(item) for item in data]
            body = json.dumps(responses).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def do_DELETE(self):
        if self.path.rstrip("/") == "/clear-responses":
            if not self.validate_token():
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'{"message": "Invalid or missing token"}')
                return

            r = get_redis_connection()
            r.delete("health_requests")
            body = json.dumps({"message": "All responses have been cleared successfully"}).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def validate_token(self):
        """Valida el token usando Redis."""
        auth_header = self.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return False

        token = auth_header.split(" ")[1]
        r = get_redis_connection()
        return r.exists(f"token:{token}") == 1

    def log_message(self, format, *args):
        return
