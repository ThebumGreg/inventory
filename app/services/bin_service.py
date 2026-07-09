from app.services.database import get_db


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


def create_bin(title, location, description):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bins (title, location, description)
        values (?, ?, ?)
    """, (title, location, description))

    conn.commit()

    bin_id = cursor.lastrowid
    conn.close()

    return bin_id


def update_bin(bin_id, title, location, description):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE bins
        SET
            title = ?,
            location = ?,
            description =?
        Where 
            id = ?
    """, (title, location, description, bin_id))

    conn.commit()
    conn.close()
    return

#delete_bin(...)

