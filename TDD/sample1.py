import unittest
from keks import keks

class KeksTest(unittest.TestCase):
	def test_createkeks(self):
		kek = keks(8)
		self.assertEqual(kek.number,8)

if __name__ == '__main__':
	unittest.main()
