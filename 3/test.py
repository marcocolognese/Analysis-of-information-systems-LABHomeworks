import unittest
from easter import easter_day

class test_easter(unittest.TestCase):

	def test_easter_day(self):
		self.assertEqual("Easter day in 2018: 1st of April", easter_day(2018))
		self.assertEqual("Easter day in 2016: 27th of March", easter_day(2016))
		self.assertEqual("Easter day in 1961: 2nd of April", easter_day(1961))
		self.assertEqual("Easter day in 1983: 3rd of April", easter_day(1983))


if __name__ == '__main__':
    unittest.main()
