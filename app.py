# -*- coding: utf-8 -*-

import http

import jinja2
from flask import Flask, jsonify

import domain_finder

app = Flask(__name__)


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
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates"),
        autoescape=jinja2.select_autoescape(["html", "xml"])
    )
    
    root_template = environment.get_template("root.html")
    return root_template.render(domain=domain_finder.find_domain())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
