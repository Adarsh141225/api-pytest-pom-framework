import configparser
import os


def get_config():
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, "..", "config.ini"))

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"CRITICAL: Cannot find config.ini at {config_path}")

    config.read(config_path)
    return config['test']