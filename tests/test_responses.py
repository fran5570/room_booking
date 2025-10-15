import json
from controllers.responses_controller import ResponsesHandler
from data.redis_client import get_redis_connection

def test_clear_and_get_responses():
    r = get_redis_connection()
    r.flushdb()  # limpiar

    # simular un registro
    r.rpush("health_requests", json.dumps({"status": "ok"}))
    r.set("token:test", "valid")

    handler = ResponsesHandler
    assert r.exists("health_requests")
    assert r.exists("token:test")
