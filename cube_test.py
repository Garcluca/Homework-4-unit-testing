import unittest
import cube

class TestCube(unittest.TestCase):

    def test_vol(self):
        self.assertEqual(cube.calculate(1,2,3),(1*2*3))
    def test_neg(self):
        self.assertEqual(cube.calculate(-1,-2,-3),(1*2*3))
    def test_zero(self):
        self.assertEqual(cube.calculate(0,0,0),(0))


unittest.main()
