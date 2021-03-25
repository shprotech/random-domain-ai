import http

from flask import Flask, jsonify

import domain_finder

app = Flask(__name__)


@app.route('/api/domain', methods=["GET"])
def hello_world():
    return jsonify({
        "url": domain_finder.find_domain(),
        "status": http.HTTPStatus.OK,
    }), http.HTTPStatus.OK


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
