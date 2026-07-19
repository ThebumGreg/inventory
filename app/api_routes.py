from flask import Blueprint, request, jsonify
from flask import current_app
import os
import json
from app.services.api_service import *

api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)

UPLOAD_FOLDER = "uploads/worklog"


@api.route("/ping")
def ping():

    return {
        "status": "ok"
    }


@api.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    
    text = file.read().decode("utf-8")

    records = [json.loads(line) for line in text.splitlines() if line.strip()]

    for record in records:
        save_work_log(record)

    return {
        "status": "ok"
        }


@api.route("/uploadphoto", methods=["POST"])
def upload_photo():

    if "photo" not in request.files:
        return {"error": "No photo"}, 400

    photo = request.files["photo"]
    iphone_path = request.form["iphone_path"]

    relative_path = iphone_path.removeprefix("iCloudDrive/Shortcuts/")

    _, extension = os.path.splitext(photo.filename)
    relative_path += extension


    filepath = os.path.join(
        current_app.config["WORKLOG_UPLOAD_FOLDER"],
        relative_path
    )

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    photo.save(filepath)

    return {
        "success": True
    }