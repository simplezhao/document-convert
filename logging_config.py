import os
import json
import logging.config
import pathlib

logging_config_dir = str(pathlib.Path(__file__).parent.absolute())


def setup_logging(
    default_path=logging_config_dir + "/" + "logging.json",
    default_level=logging.INFO,
    env_key="LOG_CFG",
):
    """Setup logging configuration"""
    config_file_path = default_path
    default_dir = "/tmp" + "/flask-app/log"
    # create default log dir
    if not os.path.exists(default_dir):
        # os.mkdir(default_dir)
        pathlib.Path(default_dir).mkdir(parents=True, exist_ok=True)

    value = os.getenv(env_key, None)
    if value:
        config_file_path = value
    if os.path.exists(config_file_path):
        with open(config_file_path, "rt", encoding="utf8") as f:
            config = json.load(f)
            config["handlers"]["info_file_handler"]["filename"] = (
                default_dir + "/info.log"
            )
            config["handlers"]["error_file_handler"]["filename"] = (
                default_dir + "/error.log"
            )

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == "__main__":
    setup_logging()
