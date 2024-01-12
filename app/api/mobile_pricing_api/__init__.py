from flask import Blueprint
import sys


sys.path.append("./app/api/mobile_pricing_api/models/Mobile_Pricing")

mobile_pricing_bp = Blueprint('mobile_pricing', __name__)


from . import view
