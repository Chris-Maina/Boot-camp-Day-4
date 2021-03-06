import unittest
from binarySearch import BinarySearch
class BinarySearchTest(unittest.TestCase):
	
	def setUp(self):
		self.one_to_ten = BinarySearch(20,1)
		self.ten_to_twenty = BinarySearch(20,2)

	def test_small list(self):
		search = self.one_to_ten.search(16)
		self.assertGreater(
			5,
			search['count'],
			msg = "should return {count : 4, index :15} for 16"
			)
		self.asserEqual(
			15,
			search['count'],
			msg = 'should return {count : 4, index :15} for 16')
	def test_large_list(self):
		search1 = self.ten_to_twenty.search(16)
		search2 = self.ten_to_twenty.search(40)
		search3 = self.ten_to_twenty.search(33)
		self.assertGreater(
			5,
			search1['count'],
			msg='should return {count: 4, index: 7} for 16'
		)
		self.assertEqual(
			7,
			search1['index'],
			msg='should return {count: 4, index: 7} for 16'
		)
		self.assertEqual(
			0,
			search2['count'],
			msg='should return {count: 0, index: 19} for 40'
		)
		self.assertEqual(
			19,
			search2['index'],
			msg='should return {count: 5, index: 19} for 40'
		)
		self.assertGreater(
			4,
			search3['count'],
			msg='should return {count: 3, index: -1} for 33'
		)
		self.assertEqual(
			-1,
			search3['index'],
			msg='should return {count: 3, index: -1} for 33'
		)
