from configparser import ConfigParser
from os.path import exists
from typing import Optional


def Config(which: Optional[str] = None):
    config = ConfigParser()

    config_filename = 'config.ini'
    if not exists(config_filename):
        print('********************************')
        print('**  Not found config file!!!  **')
        print('********************************')
        return

    config.read(config_filename)

    sections = config.sections()
    if which is None or which not in sections:
        print('******************************************')
        print(f'**  Choose config: {sections} **')
        print('******************************************')
        print('Choose config:', )
        return

    return {
        'App': {
            'app_name': config['App']['app_name'],
            'secret_key': config['App']['secret_key'],
            'host': config['App']['host'],
            'port': int(config['App']['port']),
            'reload': bool(config['App']['reload']),
            'log_level': config['App']['log_level']
        },
        'DB': {
            'host': config['DB']['host'],
            'port': int(config['DB']['port']),
            'username': config['DB']['username'],
            'password': config['DB']['password']
        }
    }[which]
