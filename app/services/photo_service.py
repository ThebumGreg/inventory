import os
from flask import current_app


def save_bin_photo(bin_id, photo):

    filename = f"{bin_id}.jpg"

    if photo.filename == "":
        return None

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    photo.save(filepath)

    return filename