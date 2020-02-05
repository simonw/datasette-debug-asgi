# datasette-debug-asgi

[![PyPI](https://img.shields.io/pypi/v/datasette-debug-asgi.svg)](https://pypi.org/project/datasette-debug-asgi/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-debug-asgi.svg?style=svg)](https://circleci.com/gh/simonw/datasette-debug-asgi)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-debug-asgi/blob/master/LICENSE)

Datasette plugin to help debug ASGI applications

Adds a new URL at `/-/asgi-scope` which shows the current ASGI scope.

Inspired by [asgi-scope](https://github.com/simonw/asgi-scope).

## Installation

    pip install datasette-debug-asgi
