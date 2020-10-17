import unittest
from unittest.mock import patch
from webreq import radio
from unittest.mock import MagicMock

class TestRequests(unittest.TestCase):
	def test_req(self):
		resp1 = radio.opbfm()
		self.assertEqual(resp1,200)

class TestRequestsMock(unittest.TestCase):
	@patch('requests.get')
	def test_some(self,mock_api_call):
		mock_api_call.return_value = MagicMock(status_code = 200)
		resp2 = radio.opbfm()
		self.assertEqual(resp2,200)

if __name__ == '__main__':
	unittest.main()