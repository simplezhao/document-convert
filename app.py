from flask_cors import CORS
from flask import Flask, jsonify

from logging_config import setup_logging
import logging as logger
from sentry_init import sentry_init
from views.convert import convert_blueprint

setup_logging()
sentry_init()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# 10M
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 10
# support document type
app.config["UPLOAD_EXTENSIONS"] = [
    ".docx",
    ".doc",
    ".xlsx",
    ".xls",
    ".ppt",
    ".pptx",
    ".md",
]
app.register_blueprint(convert_blueprint)

CORS(app)


# Return validation errors as JSON
@app.errorhandler(422)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.errorhandler(400)
@app.errorhandler(404)
def handle_error(err):
    if isinstance(err.description, str):
        return err.description, err.code
    return jsonify(error=err.description), err.code


@app.route("/", methods=["GET"])
def index():
    return jsonify("ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
