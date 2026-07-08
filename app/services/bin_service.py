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

    items = conn.execute("""
        SELECT *
        FROM items
        WHERE bin_id = ?
        ORDER BY name
    """, (bin_id,)).fetchall()

    conn.close()

    return bin, items


#create_bin(...)

#update_bin(...)

#delete_bin(...)

