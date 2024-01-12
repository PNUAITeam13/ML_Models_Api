from flask import Blueprint
from marshmallow import ValidationError

al_co_bp = Blueprint('al_co', __name__)


from . import view
