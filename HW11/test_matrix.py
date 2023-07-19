import unittest
import task4


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        arr1 = task4.Matrix([[1, 2, 3], [1, 3, 4]])
        arr2 = task4.Matrix([[2, 3], [5, 6], [3, 4]])
        arr3 = task4.Matrix([[2, 3], [5, 6], [3, 4]])
        self.assertFalse(arr1 == arr2)
        self.assertTrue(arr3 == arr2)

    def test_type(self):
        self.assertRaises(TypeError, task4.Matrix, 1, 2)

if __name__ == '__main__':
    unittest.main()

