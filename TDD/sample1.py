import unittest
from keks import keks
from wut import Wut
from douge import douge

class KeksTest(unittest.TestCase):
	def test_createkeks(self):
		kek = keks(8)
		self.assertEqual(kek.number,8)
		self.assertEqual(kek.douge,None)



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

class DougeTest(unittest.TestCase):
	def test_getdouge(self):
		douge1 = douge('kevin')
		self.assertEqual(douge1.name,'kevin')
		self.assertEqual(douge1.keks,None)

class DougeToKeksTest(unittest.TestCase):
	def test_assighnDougetoKek(self):
		kek1 = keks(7)
		douge1 = douge('kevin')
		kek1.douge = douge1
		douge1.keks = kek1
		self.assertEqual(kek1.douge,douge1)
		self.assertEqual(douge1.keks,kek1)

if __name__ == '__main__':
	unittest.main()