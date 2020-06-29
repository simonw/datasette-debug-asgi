from pprint import pformat
from datasette import hookimpl


@hookimpl
def asgi_wrapper(datasette):
    def wrap_with_asgi_auth(app):
        async def wrapped_app(scope, recieve, send):
            if scope["type"] == "http" and scope.get("path") == "/-/asgi-scope":
                await send(
                    {
                        "type": "http.response.start",
                        "status": 200,
                        "headers": [[b"content-type", b"text/plain; charset=UTF-8"],],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": pformat(scope).encode("utf8"),
                    }
                )
            else:
                await app(scope, recieve, send)

        return wrapped_app

    return wrap_with_asgi_auth
