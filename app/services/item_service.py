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

def create_item(bin_id, item_name, quantity, notes):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO items (bin_id, name, quantity, notes)
        values (?, ?, ?, ?)
    """, (bin_id, item_name, quantity, notes))

    conn.commit()
    conn.close()

    return bin_id


def get_item(item_id):

    conn = get_db()

    item_detail = conn.execute("""
        SELECT *
        FROM items
        WHERE id = ?
    """, (item_id,)).fetchone()


    conn.commit()
    conn.close()

    return item_detail

def update_item(item_name, item_quantity, item_notes, item_id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE items
        SET
            name = ?,
            quantity = ?,
            notes = ?
        Where 
            id = ?
    """, (item_name, item_quantity, item_notes, item_id))

    conn.commit()
    conn.close()
    return


def delete_item(item_id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM items
        Where 
            id = ?
    """, (item_id,))

    conn.commit()
    conn.close()
    return


