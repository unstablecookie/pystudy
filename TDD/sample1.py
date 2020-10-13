import unittest
from keks import keks
from wut import Wut

class KeksTest(unittest.TestCase):
	def test_createkeks(self):
		kek = keks(8)
		self.assertEqual(kek.number,8)



class TopsTest(unittest.TestCase):
	def test_gettops(self):
		wut = Wut()
		tops = wut.get_gettops()
		self.assertCountEqual(tops,[])
	def test_add_tops(self):
		wut = Wut()
		kek = keks(123)
		wut.addkeks(kek)
		tops = wut.get_gettops()

		self.assertEqual(tops[0],kek)

if __name__ == '__main__':
	unittest.main()