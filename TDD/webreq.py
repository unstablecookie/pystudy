import requests

class radio:
	def opbfm():
		resp1 = requests.get('http://bfm.ru')
		if resp1.ok:
			return resp1.status_code
		else:
			return 'bed resp UwU'