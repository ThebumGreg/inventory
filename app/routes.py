from flask import Blueprint, render_template, request, redirect

from app.services.bin_service import *
from app.services.item_service import *
from app.services.photo_service import *


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
        bin_name = request.form["bin_name"]
        location = request.form["location"]
        description = request.form["description"]
        bin_id = create_bin(bin_name, location, description)
        return redirect(f"/bin/{bin_id}")


@main.route("/bin/<int:bin_id>/item/new", methods=["GET","POST"])
def new_item(bin_id):

    if request.method == 'GET':
        return render_template("new_item.html")

    if request.method == 'POST':

        item_name = request.form["item_name"]
        quantity = request.form["quantity"]
        notes = request.form["notes"]
        create_item(bin_id, item_name, quantity, notes)
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

        action = request.form["action"]

        if action == "update":

            bin_name = request.form["bin_name"]
            location = request.form["location"]
            description = request.form["description"]

            photo = request.files.get("photo")

            if photo:
                filename = save_bin_photo(bin_id, photo)

                update_bin(bin_id, bin_name, location, description, filename)
            
            else:
                update_bin(bin_id, bin_name, location, description)

            return redirect(f"/bin/{bin_id}")

        if action == "delete":

            delete_bin(bin_id)
            
            bins = get_all_bins()

            return render_template(
            "bins.html",
            bins=bins
            )


@main.route("/item/<int:item_id>/edit", methods=["GET","POST"])
def edit_item(item_id):

    if request.method == 'GET':

        item_details = get_item(item_id)

        return render_template(
            "edit_item.html",
            item=item_details
        )
        
    if request.method == 'POST':

        action = request.form["action"]
        item_details = get_item(item_id)
        bin_id = item_details["bin_id"]


        if action == "update":

            item_name = request.form['item_name']
            item_quantity = request.form['item_quantity']
            item_notes = request.form['item_notes']

            update_item(item_name, item_quantity, item_notes, item_id)

        elif action == "delete":

            delete_item(item_id)

        return redirect(f"/bin/{bin_id}")