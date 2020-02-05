import pytest
import httpx
from datasette_debug_asgi import asgi_wrapper


async def app(scope, recieve, send):
    pass


@pytest.mark.asyncio
async def test_datasette_debug_asgi():
    wrapped_app = asgi_wrapper(None)(app)
    async with httpx.AsyncClient(app=wrapped_app) as client:
        response = await client.get("http://localhost/-/asgi-scope")
        assert 200 == response.status_code
        assert "text/plain; charset=UTF-8" == response.headers["content-type"]
        assert {
            "asgi": {"version": "3.0"},
            "client": ("127.0.0.1", 123),
            "headers": [
                (b"host", b"localhost"),
                (b"user-agent", b"python-httpx/0.11.1"),
                (b"accept", b"*/*"),
                (b"accept-encoding", b"gzip, deflate"),
                (b"connection", b"keep-alive"),
            ],
            "http_version": "1.1",
            "method": "GET",
            "path": "/-/asgi-scope",
            "query_string": b"",
            "root_path": "",
            "scheme": "http",
            "server": "localhost",
            "type": "http",
        } == eval(response.content)
