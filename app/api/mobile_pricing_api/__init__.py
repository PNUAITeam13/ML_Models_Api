from flask import Blueprint
from marshmallow import ValidationError
import sys


sys.path.append("./app/api/mobile_pricing_api/model/Mobile_Pricing")

mobile_pricing_bp = Blueprint('mobile_pricing', __name__)


from . import view
