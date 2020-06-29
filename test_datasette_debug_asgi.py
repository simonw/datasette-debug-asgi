from asgi_lifespan import LifespanManager
from datasette.app import Datasette
import pytest
import httpx


@pytest.mark.asyncio
async def test_datasette_debug_asgi():
    ds = Datasette([], memory=True)
    app = ds.app()
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app) as client:
            response = await client.get("http://localhost/-/asgi-scope")
            assert 200 == response.status_code
            assert "text/plain; charset=UTF-8" == response.headers["content-type"]
            assert {
                "asgi": {"version": "3.0"},
                "client": ("127.0.0.1", 123),
                "headers": [
                    (b"host", b"localhost"),
                    (
                        b"user-agent",
                        b"python-httpx/" + httpx.__version__.encode("utf-8"),
                    ),
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
