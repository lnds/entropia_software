import unittest
from main import *

class Euler1Test(unittest.TestCase):

  def test_euler(self):
    self.assertEqual(main(0), 0)
    self.assertEqual(main(4), 3)
    self.assertEqual(main(6), 8)
    self.assertEqual(main(10), 23)
    self.assertEqual(main(100), 2318)
    self.assertEqual(main(1000), 233168)
