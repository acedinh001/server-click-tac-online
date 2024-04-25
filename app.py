import os
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

from db import db

import models

from resources.profile import blp as ProfileBlueprint
from resources.setting import blp as SettingBlueprint
from resources.device import blp as DeviceBlueprint
from resources.keyword import blp as KeywordBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Server Click Tặc Online"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(ProfileBlueprint, name="profile")
    api.register_blueprint(SettingBlueprint, name="setting")
    api.register_blueprint(DeviceBlueprint, name="device")
    api.register_blueprint(KeywordBlueprint, name="keyword")

    return app
