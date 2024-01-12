from flask import Blueprint
import sys


sys.path.append("./app/api/csgo_round_winner_api/model/Mobile_Pricing")

csgo_round_winner_bp = Blueprint('csgo_round_winner', __name__)


from . import view
