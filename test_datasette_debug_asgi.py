from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_datasette_debug_asgi():
    ds = Datasette([], memory=True)
    response = await ds.client.get("/-/asgi-scope")
    assert 200 == response.status_code
    assert "text/plain; charset=UTF-8" == response.headers["content-type"]
    assert {
        "asgi": {"version": "3.0"},
        "http_version": "1.1",
        "method": "GET",
        "path": "/-/asgi-scope",
        "type": "http",
    }.items() <= eval(response.content).items()
