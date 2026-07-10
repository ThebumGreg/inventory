from app.services.database import get_db
from app.services.uuid_service import generate_uuid


def get_all_bins():

    conn = get_db()

    bins = conn.execute("""
        SELECT *
        FROM bins
        ORDER BY id
    """).fetchall()

    conn.close()

    return bins


def get_bin_details(bin_id):

    conn = get_db()

    bin = conn.execute("""
        SELECT *
        FROM bins
        WHERE id = ?
    """, (bin_id,)).fetchone()

    conn.close()

    return bin


def create_bin(bin_name, location, description):

    qr_code = generate_uuid()

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bins (bin_name, location, description, qr_code )
        values (?, ?, ?, ?)
    """, (bin_name, location, description, qr_code))

    conn.commit()

    bin_id = cursor.lastrowid
    conn.close()

    return bin_id


def update_bin(bin_id, bin_name, location, description, photo_filename=None):

    conn = get_db()
    cursor = conn.cursor()

    if photo_filename:

        cursor.execute("""
            UPDATE bins
            SET
                bin_name = ?,
                location = ?,
                description = ?,
                photo_filename =?,
                updated_at = CURRENT_TIMESTAMP
            Where 
                id = ?
        """, (bin_name, location, description, photo_filename, bin_id))

    else:

        cursor.execute("""
            UPDATE bins
            SET
                bin_name = ?,
                location = ?,
                description = ?,
                updated_at = CURRENT_TIMESTAMP
            Where 
                id = ?
        """, (bin_name, location, description, bin_id))

    conn.commit()
    conn.close()
    return

def delete_bin(bin_id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM items
        Where bin_id = ?
    """, (bin_id,))

    cursor.execute("""
        DELETE FROM bins
        Where id = ?
    """, (bin_id,))

    conn.commit()
    conn.close()
    return
