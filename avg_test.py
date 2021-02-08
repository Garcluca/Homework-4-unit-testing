import unittest
import avg

class TestAvg(unittest.TestCase):

    def test_avg(self):
        arr = [10,10,10,10]
        self.assertEqual(avg.calculate(arr),10)
    def test_neg(self):
        arr = [-1]
        self.assertEqual(avg.calculate(arr),-1)
    def test_zero(self):
        arr = [0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(avg.calculate(arr),0)

#if __name__ = '__main__':
unittest.main()
