from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("path", ("/-/asgi-scope", "/-/asgi-scope/blah"))
async def test_datasette_debug_asgi(path):
    ds = Datasette([], memory=True)
    response = await ds.client.get(path)
    assert 200 == response.status_code
    assert "text/plain; charset=utf-8" == response.headers["content-type"]
    lines = response.text.split("\n")
    # Remove the csrftoken line, it won't eval() correctly
    lines = [l for l in lines if "csrftoken" not in l]
    assert {
        "asgi": {"version": "3.0"},
        "http_version": "1.1",
        "method": "GET",
        "path": path,
        "type": "http",
    }.items() <= eval("\n".join(lines)).items()
