from pathlib import Path
import yaml

__all__ = ('load_config') # limit function call

def load_config(config_file=None):
	default_file = Path(__file__).parent / 'config.yaml' #reading default config file
	with open(default_file, 'r') as f1:
		config = yaml.safe_load(f1)

#	cf_dict = {}
#	if config_file:
#		cf_dict = yaml.safe_load(config_file) # updating some keys with new config file, if needed

#	config = yaml.update(**cf_dict)

	return config