# -*- coding: utf-8 -*-
"""
Author: shaharmelamed
Created: 3/25/2021
Description: The main app.
"""
# ----- Imports ----- #

import http

from flask import Flask, jsonify, request

import domain_finder

# ----- Globals ----- #

app = Flask(__name__)

# ----- Functions ----- #


@app.route('/api/domain', methods=["GET"])
def api_get_domain():
    """
    Get a non-existing domain.

    :return: The result JSON and the status code.
    """
    return jsonify({
        "url": domain_finder.find_domain(),
        "status": http.HTTPStatus.OK,
    }), http.HTTPStatus.OK


@app.route('/', methods=["GET"])
def root_page():
    """
    Get the root page.

    :return: The content of the page and the status code.
    """
    root_template = app.jinja_env.get_template("root.html")
    dark = not request.args.get("light", False, type=bool)
    return root_template.render(domain=domain_finder.find_domain(), dark=dark)


# ----- Main Entry Point ----- #


def main():
    app.create_jinja_environment()
    app.run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    main()
