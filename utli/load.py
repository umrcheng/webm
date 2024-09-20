import json


def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        return config


CONFIG = load_config()
