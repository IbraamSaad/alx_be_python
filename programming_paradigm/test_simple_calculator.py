import unittest
from simple_calculator import SimpleCalculator



class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    

    def test_addition(self):
        self.assertEqual(self.calc.add(20,10), 30)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(20,10), 10)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(20,10), 200)

    def test_division(self):
        self.assertEqual(self.calc.divide(20,10), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)
    
    

   

if __name__ == "__main__":
    unittest.main()

           