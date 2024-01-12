from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow

from config import Config


mm = Marshmallow()
cors = CORS(supports_credentials=True, methods=["GET", "POST", "OPTIONS"])


def create_app(config_class=Config.get_config()):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    mm.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    with app.app_context():
        from .api import api_bp

        app.register_blueprint(api_bp, url_prefix='/api')

    return app


config = Config.get_config()

app = create_app(config)

