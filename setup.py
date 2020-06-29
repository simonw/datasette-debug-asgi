from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-debug-asgi",
    description="Datasette plugin for dumping out the ASGI scope",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-debug-asgi",
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["datasette_debug_asgi"],
    entry_points={"datasette": ["debug_asgi = datasette_debug_asgi"]},
    extras_require={
        "test": ["datasette", "pytest", "pytest-asyncio", "httpx", "asgi-lifespan~=1.0"]
    },
    tests_require=["datasette-debug-asgi[test]"],
)
