from flask import Blueprint, render_template

from app.database import get_db

main = Blueprint("main", __name__)

@main.route("/bins")
def bins():

    conn = get_db()

    bins = conn.execute("""
        SELECT *
        FROM bins
        ORDER BY id
    """).fetchall()

    conn.close()

    return render_template(
        "bins.html",
        bins=bins
    )

@main.route("/bin/<int:bin_id>")
def bin_details(bin_id):

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

    return render_template(
        "bin.html",
        bin=bin,
        items=items
    )

@main.route("/")
def index():
    return render_template("index.html")