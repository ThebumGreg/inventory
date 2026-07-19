from app.services.database import get_db
import sqlite3
from datetime import datetime

DATABASE = "worklog.db"

def save_work_log(record):

    address = record.get("address", "").strip()
    customer = record.get("customer")
    state = record.get("state")

    timestamp = record.get("time")
    dt = datetime.fromisoformat(timestamp)

    billable = record.get("billable", "No") == "Yes"

    notes = record.get("notes")
    sitestate = record.get("sitestate")
    pics = record.get("pics")

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO work_log (
            event_time,
            customer,
            address,
            state,
            site_state,
            billable,
            notes,
            pictures
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        dt.isoformat(timespec="seconds"),
        customer,
        address,
        state,
        sitestate,
        int(billable),
        notes,
        pics
    ))

    conn.commit()



def save_worklog_photo(bin_id, photo):

    filename = f"{bin_id}.jpg"

    if photo.filename == "":
        return None

    filepath = os.path.join(
        current_app.config["WORKLOG_UPLOAD_FOLDER"],
        filename
    )

    photo.save(filepath)

    return filename



