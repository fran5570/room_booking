from http.server import HTTPServer, BaseHTTPRequestHandler
from controllers.health_controller import HealthHandler
from controllers.responses_controller import ResponsesHandler


class CombinedHandler(HealthHandler, ResponsesHandler):
    """Handler combinado para /health, /get-responses y /clear-responses."""

    def do_GET(self):
        if self.path.rstrip("/") == "/health":
            return HealthHandler.do_GET(self)
        elif self.path.rstrip("/") == "/get-responses":
            return ResponsesHandler.do_GET(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_DELETE(self):
        if self.path.rstrip("/") == "/clear-responses":
            return ResponsesHandler.do_DELETE(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def log_message(self, format, *args):
        return


def start_server():
    server = HTTPServer(("0.0.0.0", 8000), CombinedHandler)
    print("Servidor corriendo en http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido.")
        server.server_close()


if __name__ == "__main__":
    start_server()
