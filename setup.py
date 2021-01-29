from setuptools import setup
import os

VERSION = "1.0"


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
    project_urls={
        "Issues": "https://github.com/simonw/datasette-debug-asgi/issues",
        "CI": "https://github.com/simonw/datasette-debug-asgi/actions",
        "Changelog": "https://github.com/simonw/datasette-debug-asgi/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["datasette_debug_asgi"],
    entry_points={"datasette": ["debug_asgi = datasette_debug_asgi"]},
    install_requires=["datasette>=0.50"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-debug-asgi[test]"],
    python_requires=">=3.6",
)
