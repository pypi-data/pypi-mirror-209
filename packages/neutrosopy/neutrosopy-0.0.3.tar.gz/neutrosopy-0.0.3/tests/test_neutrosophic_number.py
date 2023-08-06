import unittest

from neutrosopy import NeutrosophicNumber

class NeutrosophicNumberTests(unittest.TestCase):

    def test_addition(self):
        n1 = NeutrosophicNumber(2, 3)
        n2 = NeutrosophicNumber(1, 4)
        result = n1 + n2
        self.assertEqual(result.a, 3)
        self.assertEqual(result.b, 7)

    def test_subtraction(self):
        n1 = NeutrosophicNumber(5, 2)
        n2 = NeutrosophicNumber(3, 1)
        result = n1 - n2
        self.assertEqual(result.a, 2)
        self.assertEqual(result.b, 1)

    def test_multiplication(self):
        n1 = NeutrosophicNumber(2, 3)
        n2 = NeutrosophicNumber(4, 1)
        result = n1 * n2
        self.assertEqual(result.a, 5)
        self.assertEqual(result.b, 14)

    def test_division(self):
        n1 = NeutrosophicNumber(10, 5)
        n2 = NeutrosophicNumber(2, 3)
        result = n1 / n2
        self.assertEqual(result.a, 5)
        self.assertEqual(result.b, 0.0)

    def test_power(self):
        n1 = NeutrosophicNumber(2, 3)
        result = n1 ** 2
        self.assertEqual(result.a, -5)
        self.assertEqual(result.b, 12)

    def test_absolute_value(self):
        n1 = NeutrosophicNumber(3, -4)
        result = abs(n1)
        self.assertEqual(result, 5.0)

    def test_equality(self):
        n1 = NeutrosophicNumber(2, 3)
        n2 = NeutrosophicNumber(2, 3)
        self.assertEqual(n1, n2)

    def test_inequality(self):
        n1 = NeutrosophicNumber(2, 3)
        n2 = NeutrosophicNumber(4, 5)
        self.assertNotEqual(n1, n2)

if __name__ == '__main__':
    unittest.main()

