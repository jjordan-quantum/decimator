import unittest
from decimator import Decimator

integers = [0, 1, 2, 5, 10, 11, 13, 53, 99, 100, 101, 103, 451564, 515445105, 1654651654651616]
floats = [0.0, 0.1, 0.10, 0.11, 0.213, 0.1215135, 1.0, 1.1, 1.11, 1.0000, 1.1000, 121.10, 1.3261, 13.0, 5.3, 9.9, 10.0, 101.56144564684654, 10.3, 4515.64, 5.15445105, 1.6546516546516165]
failures = [-1, -0.12, '1.13']

integer_decimators = []
float_decimators = []
failure_decimators = []



for integer in integers:
    integer_decimators.append(Decimator(integer))
for float_value in floats:
    float_decimators.append(Decimator(float_value))
for failure_value in failures:
    try:
        failure_decimators.append(Decimator(failure_value))
    except Exception as error:
        print(f'Trying to create Decimator object with {failure_value}:\n{error}\n')

class TestDecimator(unittest.TestCase):

    def test_0_str_int(self):
        """
        Test __str__ method of Decimator objects, instantiated with ints
        :return:
        """
        print('f\nIn test_0_str')
        print('--------------------------')
        for decimator in integer_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(int(decimator.integer_string)+float(decimator.fraction_string), int(string))
            self.assertEqual(int(decimator.number), decimator.get_value())

    def test_1_str_float(self):
        """
        Test __str__ method of Decimator objects, instantiated with floats
        :return:
        """
        print('f\nIn test_0_str')
        print('--------------------------')
        for decimator in float_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator string: {str(decimator)}')
            print(f'Decimator integer: {decimator.integer_string}')
            print(f'Decimator fraction: {decimator.fraction_string}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            value_a = float(int(decimator.integer_string))+float(decimator.fraction_string)
            value_b = float(string)
            difference = value_a-value_b
            print(f'Value A: {str(value_a)}')
            print(f'Value B: {str(value_b)}\n')
            self.assertTrue(abs(difference) < 10**((-1)*(decimator.fraction_precision)))




if __name__ == '__main__':
    unittest.main()

