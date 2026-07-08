from flask import Blueprint, render_template

#from app.database import get_db
from app.services.bin_service import *

main = Blueprint("main", __name__)

@main.route("/bins")
def List_bins():

    bins = get_all_bins()

    return render_template(
        "bins.html",
        bins=bins
    )

@main.route("/bin/<int:bin_id>")
def bin_details(bin_id):

    bin, items = get_bin_details(bin_id)

    return render_template(
        "bin.html",
        bin=bin,
        items=items
    )

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/bin/new")
def new_bin():
    return render_template("new_bin.html")

#@main.route("/bin/new", methods=["GET","POST"])
#def new_bin():
