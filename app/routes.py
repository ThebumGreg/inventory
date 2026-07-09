from flask import Blueprint, render_template, request, redirect

#from app.database import get_db
from app.services.bin_service import *
from app.services.item_service import *


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/bins")
def List_bins():

    bins = get_all_bins()

    return render_template(
        "bins.html",
        bins=bins
    )

@main.route("/bin/<int:bin_id>")
def bin_details(bin_id):

    bin = get_bin_details(bin_id)
    items = get_items_by_bin(bin_id)

    return render_template(
        "bin.html",
        bin=bin,
        items=items
    )

@main.route("/bin/new", methods=["GET","POST"])
def new_bin():

    if request.method == 'GET':
        return render_template("new_bin.html")
    
    if request.method == 'POST':
        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        bin_id = create_bin(title, location, description)
        return redirect(f"/bin/{bin_id}")


@main.route("/bin/<int:bin_id>/item/new", methods=["GET","POST"])
def new_item(bin_id):

    if request.method == 'GET':
        return render_template("new_item.html")

    if request.method == 'POST':
        item_name = request.form["item_name"]
        quantity = request.form["quantity"]
        notes = request.form["notes"]
        test = create_item(bin_id, item_name, quantity, notes)
        return redirect(f"/bin/{bin_id}")

@main.route("/bin/<int:bin_id>/edit", methods=["GET","POST"])
def edit_bin(bin_id):

    if request.method == 'GET':

        bin = get_bin_details(bin_id)
        items = get_items_by_bin(bin_id)

        return render_template(
            "edit_bin.html",
            bin=bin,
            items=items
        )
    if request.method == 'POST':

        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        test = update_bin(bin_id, title, location, description)
        return redirect(f"/bin/{bin_id}")




        