from configparser import ConfigParser
from os.path import exists
from typing import Optional

def Config(which: Optional[str] = None):
	config = ConfigParser()

	config_filename = 'config.ini'
	if not exists(config_filename):
		print('Not found config file!!!')
		return

	config.read(config_filename)

	if which is None or which not in config.sections():
		print('Choose config:', config.sections())
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
