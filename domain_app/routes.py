"""
Author: shaharmelamed
Date: 3/26/21
Description: The routes of the app.
"""
# ----- Imports ----- #

from datetime import datetime
import http

from flask import Blueprint, request, render_template

import domain_finder

# ----- Globals ----- #

BLUEPRINT = Blueprint("main", __name__, url_prefix=None, root_path="/")

# ----- Functions ----- #


@BLUEPRINT.app_context_processor
def inject_now():
    """
    Get the current time.
    """
    return {"now": datetime.utcnow}


@BLUEPRINT.route('/', methods=["GET"])
def root_page():
    """
    Get the root page.

    :return: The content of the page and the status code.
    """
    dark = not request.args.get("light", False, type=bool)
    return render_template("root.html",
                           domain=domain_finder.find_domain(), dark=dark), http.HTTPStatus.OK
