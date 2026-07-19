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

    #filename = secure_filename(photo.filename)
    filename = photo.filename

    filepath = os.path.join(
        current_app.config["WORKLOG_UPLOAD_FOLDER"],
        filename
    )

    photo.save(filepath)


    #filename = f"{uuid.uuid4()}_{filename}"

    #filepath = os.path.join(WORKLOG_UPLOAD_FOLDER, filename)

    #photo.save(filepath)

    return {
        "success": True,
        "filename": filename
    }