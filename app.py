# -*- coding: utf-8 -*-
"""
Author: shaharmelamed
Created: 3/25/2021
Description: The main app.
"""
# ----- Imports ----- #

from flask import Flask

import domain_app

# ----- Globals ----- #

app = Flask(__name__)

# ----- Main Entry Point ----- #


def main():
    app.create_jinja_environment()
    app.register_blueprint(domain_app.BLUEPRINT)
    app.register_blueprint(domain_app.api.BLUEPRINT)
    app.run(host="0.0.0.0", port=80, threaded=True)


main()
