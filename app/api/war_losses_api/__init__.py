from flask import Blueprint
import sys


sys.path.append("./app/api/war_losses_api/models/war_losses")


war_losses_bp = Blueprint('war_losses', __name__)

from . import view
