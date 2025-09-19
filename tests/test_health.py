import json
import socket
import time
from http.client import HTTPConnection

from controllers.health_controller import start_health_server


def _free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def test_health_endpoint_ok_and_fast():
    port = _free_port()
    server, _thread = start_health_server(port=port)

    try:
        t0 = time.perf_counter()

        conn = HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("GET", "/health")
        resp = conn.getresponse()

        elapsed_ms = (time.perf_counter() - t0) * 1000

        assert resp.status == 200
        data = json.loads(resp.read())
        assert data.get("status") == "ok"
        assert "timestamp" in data
        assert elapsed_ms < 100, f"Health tardó {elapsed_ms:.1f} ms"
    finally:
        server.shutdown()
        server.server_close()
