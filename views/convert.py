import subprocess
from tempfile import TemporaryDirectory
from flask import Blueprint, request, send_from_directory
import logging as logger
from flask import current_app
from views.serializer import ConvertSerializer
from webargs.flaskparser import use_args
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import jsonify
import os
from sentry_sdk import capture_exception
from werkzeug.utils import secure_filename

convert_blueprint = Blueprint("convert", __name__, url_prefix="/convertApi")


def download_file(bucket_name, filename, download_path):
    pass


def upload_file(bucket_name, file_path, file_name):
    pass


def convert_to_pdf(file):
    # try:
    #     subprocess.check_call(["unoconv", "-f", "pdf", file])
    #     return True

    # except Exception as e:
    #     logger.error(e)
    #     return False
    subprocess.check_call(["unoconv", "-f", "pdf", file])


def convert_to_any(file, convert_type="pdf"):
    logger.info(f"file name: {file}, convert type to: {convert_type}")
    subprocess.check_call(["unoconv", "-f", convert_type, file])
    return os.path.splitext(file)[0] + "." + convert_type


@convert_blueprint.route("/v1/convert", methods=["POST"])
# @use_args(ConvertSerializer, location="json")
def convert():
    try:

        if "file" not in request.files:
            return jsonify({"status": -1, "error": "No file part"}), 400

        convert_file = request.files["file"]
        filename = convert_file.filename
        if not filename:
            return jsonify({"status": -1, "error": "Filename not found"}), 400

        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config["UPLOAD_EXTENSIONS"]:
            logger.info(f"file type is {file_ext}")
            return jsonify({"status": -1, "error": "File type not support"}), 400

        convert_type = request.form.get("convertType", "pdf")

        with TemporaryDirectory() as temp_dir:
            secure_temp_file = temp_dir + "/" + secure_filename(filename)
            convert_file.save(secure_temp_file)
            converted_file = convert_to_any(secure_temp_file, convert_type=convert_type)
            # logger.info(converted_file)
            # logger.info(os.path.split(converted_file)[1])
            return send_from_directory(
                os.path.split(converted_file)[0], os.path.split(converted_file)[1]
            )

    except Exception as e:
        logger.error(e)
        capture_exception(e)
        return jsonify({"status": -1, "error": "Internal Server Error"}), 500


if __name__ == "__main__":
    pass
