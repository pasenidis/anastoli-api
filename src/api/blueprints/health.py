from quart import Blueprint, current_app as app, jsonify
from logbook import Logger

log = Logger(__name__)
bp = Blueprint("health", __name__)


@bp.route('/')
async def health():
    return jsonify({"message": "hi"})
