from datasette import hookimpl
from datasette.utils.asgi import Response
from pprint import pformat


def asgi_scope(scope):
    return Response.text(pformat(scope))


@hookimpl
def register_routes():
    return (("^/-/asgi-scope$", asgi_scope),)
