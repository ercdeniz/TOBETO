import configparser


def read_config(key):
    config = configparser.ConfigParser()
    config.read('../config.properties')
    value = config['DEFAULT'][key]
    return value
