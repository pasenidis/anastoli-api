import logbook
import logging
import sys
import quart_openapi
import tracemalloc
import asyncio
import traceback
from quart import Quart, Response, jsonify, flask_patch
from databases import Database
from termcolor import colored
from typing import Union, Tuple
from logging import Formatter

from api.errors import APIError
from api.blueprints import (
    health
)

import config

tracemalloc.start()

colors = {
    logbook.CRITICAL: "red",
    logbook.ERROR: "red",
    logbook.WARNING: "yellow",
    logbook.NOTICE: "yellow",
    logbook.DEBUG: "white",
    logbook.TRACE: "red"
}


class ColoredHandler(logbook.StreamHandler):
    def format(self, record):
        rv = super(ColoredHandler, self).format(record)
        color = colors.get(record.level)
        return colored(rv, color) if color else rv


handler = ColoredHandler(sys.stdout, level=logbook.INFO)
handler.push_application()

log = logbook.Logger("quart_boilerplate")
logbook.compat.redirect_logging()

app = Quart(__name__)
app.config.from_object(f"config.{config.MODE}")
is_debug = app.config.get("DEBUG_MODE", False)
app.debug = is_debug

if is_debug:
    handler.level = logbook.DEBUG
    app.logger.level = logbook.DEBUG
    log.debug("Debug mode is enabled")

blueprints = {
    health: "/health"
}

for blueprint, suffix in blueprints.items():
    app.register_blueprint(blueprint, url_prefix=suffix or "")


@app.before_serving
async def app_before_serving():
    app.loop = asyncio.get_event_loop()


@app.after_serving
async def app_after_serving():
    tracemalloc.stop()


@app.errorhandler(APIError)
async def handle_api_error(error: APIError) -> Tuple[Response, int]:
    resp = {}

    if error.json:
        resp.update({**error.json})

    if error.message:
        resp.update({"message": error.message})

    error_code = getattr(error, "error_code", None)

    if error_code:
        resp.update({"error_code": error_code})

    return jsonify(resp), error.status_code
