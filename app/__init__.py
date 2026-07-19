from flask import Flask
import os

def create_app():

    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = os.path.join(
    app.static_folder,
    "uploads",
    "bins"
    )

    app.config["WORKLOG_UPLOAD_FOLDER"] = os.path.join(
    app.static_folder,
        "uploads",
        "worklog"
    )



    app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    os.makedirs(
        app.config["WORKLOG_UPLOAD_FOLDER"],
        exist_ok=True
    )

    from .routes import main

    app.register_blueprint(main)

    from .api_routes import api

    app.register_blueprint(api)

    return app