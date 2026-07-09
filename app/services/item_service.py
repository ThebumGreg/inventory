from app.services.database import get_db

def get_items_by_bin(bin_id):

    conn = get_db()

    items = conn.execute("""
        SELECT *
        FROM items
        WHERE bin_id = ?
        ORDER BY name
    """, (bin_id,)).fetchall()

    return items




