import configparser
import json


def read_config(key):
    config = configparser.ConfigParser()
    config.read('../config.properties')
    value = config['DEFAULT'][key]
    return value


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [(account["type"], account["url"]) for account in data["accounts"]]