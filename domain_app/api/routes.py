"""
Author: shaharmelamed
Date: 3/26/21
Description: The routes of the API.
"""
# ----- Imports ----- #

import http

from flask import Blueprint, jsonify

import domain_finder

# ----- Globals ----- #

BLUEPRINT = Blueprint("api", __name__, url_prefix="/api")

# ----- Functions ----- #


@BLUEPRINT.route('/domain', methods=["GET"])
def api_get_domain():
    """
    Get a non-existing domain.

    :return: The result JSON and the status code.
    """
    return jsonify({
        "url": domain_finder.find_domain(),
        "status": http.HTTPStatus.OK,
    }), http.HTTPStatus.OK
