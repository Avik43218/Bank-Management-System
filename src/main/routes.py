from flask import Blueprint, render_template
from flask_login import current_user

from src import limiter

main = Blueprint('main', __name__)

@main.route("/")
@limiter.exempt
def root_route():

    if current_user.is_authenticated:
        return render_template("dashboard.html", title="Dashboard")

    return render_template("home.html", title="Home")


@main.route("/about_us")
@limiter.exempt
def about_us():

    return render_template("about_us.html", title="About Us")


@main.route("/support")
@limiter.exempt
def support():
    
    return render_template("Support.html", title="Support")
