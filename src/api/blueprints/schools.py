from quart import Blueprint, current_app as app, jsonify
from logbook import Logger
from scrapper import total_schools
from api.search import research
import json

log = Logger(__name__)
bp = Blueprint("schools", __name__)


@bp.route('/')
@bp.route('/search')
async def schools():
    t = total_schools()
    return jsonify({"schools": t[1]})

@bp.route('/search/<school>')
async def search(school):
    t = total_schools()
    t = research(school, t[1])

    return jsonify({"school": t})