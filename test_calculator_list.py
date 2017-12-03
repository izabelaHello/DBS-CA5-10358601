# Created on Sun Dec 03
# Author: 10358601 Izabela Tyrna

###This is a program that test calcualtor_list.py


import unittest
from calculator_list import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([1,2,3,4], [1,2,3,5])
        self.assertEqual([2, 4, 6, 9], result)
        result = self.calc.add([1,2,3,4], [1,2,3,5,6])
        self.assertEqual(None, result)
        
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([1,2,3,4], [1,2,3,5])
        self.assertEqual([0, 0, 0, -1], result)
        
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([1,2,3,4], [1,2,3,5])
        self.assertEqual([1, 4, 9, 20], result)    

    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide([1,2,3,4], [1,2,3,5])
        self.assertEqual([1.0, 1.0, 1.0, 0.8], result)
        result = self.calc.divide([1,2,3,4], [1,2,0,-5])
        self.assertEqual(None, result)

    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([1,2,3,4])
        self.assertEqual([1, 4, 9, 16], result)

    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube([1,2,3,5])
        self.assertEqual([1, 8, 27, 125], result)
        
    def test_calculator_squareroot_method_returns_correct_result(self):
        result = self.calc.squareroot([1,2,3,5])
        self.assertEqual([1.0, 1.4142135623730951, 1.7320508075688772, 2.23606797749979], result)  
        result = self.calc.squareroot([1,2,0,-5])
        self.assertEqual(None, result) 

    def test_calculator_power_method_returns_correct_result(self):
        result = self.calc.power([1,2,3,4], [1,2,3,5])
        self.assertEqual([1.0, 4.0, 27.0, 1024.0], result)
        
    def test_calculator_factorial_method_returns_correct_result(self):
        result = self.calc.factorial([1,2,3,4])
        self.assertEqual([1, 2, 6, 24], result)
    
    def test_calculator_sin_method_returns_correct_result(self):
        result = self.calc.sin([1,2,3,4])
        self.assertAlmostEqual([0.8414709, 0.9092974, 0.1411200, -0.7568024], result)
    

if __name__ == '__main__':
    unittest.main()