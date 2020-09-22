from quart import Blueprint, current_app as app, jsonify
from logbook import Logger
from scrapper import total_schools
import json

log = Logger(__name__)
bp = Blueprint("schools", __name__)


@bp.route('/')
async def schools():
    t = total_schools()
    return jsonify({"schools": t[1]})
