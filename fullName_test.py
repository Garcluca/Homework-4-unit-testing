import unittest
import fullName

class TestAvg(unittest.TestCase):

    def test_avg(self):
        a = "Jon"
        b = "Smith"

        self.assertEqual(fullName.calculate(a,b),"Jon Smith")
    def test_neg(self):
        a = "Larry   " 
        b = "Page"
        self.assertEqual(fullName.calculate(a,b),"Larry Page")
    def test_zero(self):
        a = "Lucas"
        b = ""
        self.assertEqual(fullName.calculate(a,b),"Lucas ")

#if __name__ = '__main__':
unittest.main()
