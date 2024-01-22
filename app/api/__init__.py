from flask import Blueprint
from marshmallow import ValidationError


api_bp = Blueprint('api', __name__)


from .alcohol_consumption_api import al_co_bp
from .mobile_pricing_api import mobile_pricing_bp
from .csgo_round_winner_api import csgo_round_winner_bp
from .war_losses_api import war_losses_bp

api_bp.register_blueprint(al_co_bp, url_prefix="/alcohol_consumption")
api_bp.register_blueprint(mobile_pricing_bp, url_prefix="/mobile_pricing")
api_bp.register_blueprint(csgo_round_winner_bp, url_prefix="/csgo_round_winner")
api_bp.register_blueprint(war_losses_bp, url_prefix="/war_losses")


# @api_bp.app_errorhandler(ValueError)
# def handle_marshmallow_error(e):
#     return "Expected object or value", 400


# @api_bp.app_errorhandler(KeyError)
# def handle_marshmallow_error(e):
#     return "The data you submitted does not contain the required fields", 400


# @api_bp.app_errorhandler(ValidationError)
# def handle_marshmallow_error(e):
#     return e.messages, 400
