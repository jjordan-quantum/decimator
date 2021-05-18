import unittest
from decimator import Decimator

# numeric constructor arguments
integers = [0, 1, 2, 5, 10, 11, 13, 53, 99, 100, 101, 103, 451564, 515445105, 1654651654651616]
floats = [0.0, 0.1, 0.10, 0.11, 0.213, 0.1215135, 1.0, 1.1, 1.11, 1.0000, 1.1000, 121.10, 1.3261, 13.0, 5.3, 9.9, 10.0, 10111.56144564684654, 10.3, 4515.64, 5.15445105, 1.6546516546516165]
failures = [-1, -0.12]

# string constructor arguments
integer_strings = ['0', '1', '2', '5', '10', '11', '13', '53', '99', '100', '101', '103', '451564', '515445105', '1654651654651616']
float_strings = ['0.0', '0.1', '0.10', '0.11', '0.213', '0.1215135', '1.0', '1.1', '1.11', '1.0000', '1.1000', '121.10', '1.3261', '13.0', '5.3', '9.9', '10.0', '10111.56144564684654', '10.3', '4515.64', '5.15445105', '1.654651654651616']
failure_strings = ['-1', '-0.12']

# lists for decimators with numeric constructor args
integer_decimators = []
float_decimators = []
failure_decimators = []

# lists for decimators with string constructor args
integer_string_decimators = []
float_string_decimators = []
failure_string_decimators = []

# instantiate decimators with numeric constructor args
for integer in integers:
    integer_decimators.append(Decimator(integer))
for float_value in floats:
    float_decimators.append(Decimator(float_value))
for failure_value in failures:
    try:
        failure_decimators.append(Decimator(failure_value))
    except Exception as error:
        print(f'Trying to create Decimator object with {failure_value}:\n{error}\n')

# instantiate decimators with string constructor args
for integer_string in integer_strings:
    integer_string_decimators.append(Decimator(integer_string))
for float_string in float_strings:
    float_string_decimators.append(Decimator(float_string))
for failure_string in failure_strings:
    try:
        failure_string_decimators.append(Decimator(failure_string))
    except Exception as error:
        print(f'Trying to create Decimator object with {failure_string}:\n{error}\n')

class TestDecimator(unittest.TestCase):

    def test_0_num_int(self):
        """
        Use __str__ method of Decimator objects to test validity of data structures
        for Decimators instantiated with int's
        """
        print('f\nIn test_0_num_int')
        print('--------------------------')
        for decimator in integer_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(int(decimator.integer_string)+float(decimator.fraction_string), int(string))

    def test_1_num_float(self):
        """
        TUse __str__ method of Decimator objects to test validity of data structures
        for Decimators instantiated with floats
        """
        print('f\nIn test_1_num_float')
        print('--------------------------')
        for decimator in float_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator string: {str(decimator)}')
            print(f'Decimator float string: {float(str(decimator))}')
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

    def test_2_str_int(self):
        """
        Use __str__ method of Decimator objects to test validity of data structures
        for Decimators instantiated with int strings
        """
        print('f\nIn test_2_str_int')
        print('--------------------------')
        for decimator in integer_string_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(int(decimator.integer_string)+float(decimator.fraction_string), int(string))

    def test_3_str_float(self):
        """
        Use __str__ method of Decimator objects to test validity of data structures
        for Decimators instantiated with float strings
        """
        print('f\nIn test_3_str_float')
        print('--------------------------')
        for decimator in float_string_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator string: {str(decimator)}')
            print(f'Decimator float string: {float(str(decimator))}')
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

    ########################################################
    # get_value

    def test_4_get_value_num_int(self):
        """
        Test get_value method of Decimator objects
        """
        print('f\nIn test_4_get_value_num_int')
        print('--------------------------')
        for decimator in integer_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(decimator.number, decimator.get_value())

    def test_5_get_value_num_float(self):
        """
        Test get_value method of Decimator objects
        """
        print('f\nIn test_5_get_value_num_float')
        print('--------------------------')
        for decimator in float_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator string: {str(decimator)}')
            print(f'Decimator float string: {float(str(decimator))}')
            print(f'Decimator integer: {decimator.integer_string}')
            print(f'Decimator fraction: {decimator.fraction_string}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(decimator.number, decimator.get_value())

    def test_6_get_value_str_int(self):
        """
        Test get_value method of Decimator objects
        """
        print('f\nIn test_6_get_value_str_int')
        print('--------------------------')
        for decimator in integer_string_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(int(decimator.number), decimator.get_value())

    def test_7_get_value_str_float(self):
        """
        Test get_value method of Decimator objects
        """
        print('f\nIn test_7_get_value_str_float')
        print('--------------------------')
        for decimator in float_string_decimators:
            print(f'Decimator number: {decimator.number}')
            print(f'Decimator string: {str(decimator)}')
            print(f'Decimator float string: {float(str(decimator))}')
            print(f'Decimator integer: {decimator.integer_string}')
            print(f'Decimator fraction: {decimator.fraction_string}')
            print(f'Decimator positive_decimals: {decimator.positive_decimals}')
            print(f'Decimator negative_decimals: {decimator.negative_decimals}')
            string = str(decimator)
            self.assertEqual(float(decimator.number), decimator.get_value())

    ########################################################
    # shift

    def test_8_shift_positive_num_int(self):
        """
        Test shift method of Decimator objects, with positive shift for numeric int constructor args
        """
        print('f\nIn test_8_shift_positive_num_int')
        print('--------------------------')
        shifts = [0,1,2,3,10,20]
        for decimator in integer_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                self.assertEqual(decimator.get_value()*10**shift, shifted_decimator.get_value())

    def test_9_shift_negative_num_int(self):
        """
        Test shift method of Decimator objects, with negative shift for numeric int constructor args
        """
        print('f\nIn test_9_shift_negative_num_int')
        print('--------------------------')
        shifts = [-1,-2,-3,-10,-20]
        for decimator in integer_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                self.assertTrue(abs(difference) < 10 ** ((-1) * (shifted_decimator.fraction_precision)))

    def test_10_shift_positive_num_float(self):
        """
        Test shift method of Decimator objects, with positive shift for numeric float constructor args
        """
        print('f\nIn test_10_shift_positive_num_float')
        print('--------------------------')
        shifts = [0,1,2,3,10,20]
        for decimator in float_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                self.assertTrue(abs(difference) < 10 ** max(shift-15, shift-decimator.fraction_precision))

    def test_11_shift_negative_num_float(self):
        """
        Test shift method of Decimator objects, with negative shift for numeric float constructor args
        """
        print('f\nIn test_11_shift_negative_num_float')
        print('--------------------------')
        shifts = [-1,-2,-3,-10,-20]
        for decimator in float_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                self.assertTrue(abs(difference) < 10 ** ((-1) * (shifted_decimator.fraction_precision - 1)))

    def test_12_shift_positive_string_int(self):
        """
        Test shift method of Decimator objects, with positive shift for string int constructor args
        """
        print('f\nIn test_12_shift_positive_string_int')
        print('--------------------------')
        shifts = [0,1,2,3,10,20]
        for decimator in integer_string_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                self.assertEqual(decimator.get_value()*10**shift, shifted_decimator.get_value())

    def test_13_shift_negative_string_int(self):
        """
        Test shift method of Decimator objects, with negative shift for string int constructor args
        """
        print('f\nIn test_13_shift_negative_string_int')
        print('--------------------------')
        shifts = [-1,-2,-3,-10,-20]
        for decimator in integer_string_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                self.assertTrue(abs(difference) < 10 ** ((-1) * (shifted_decimator.fraction_precision)))

    def test_14_shift_positive_string_float(self):
        """
        Test shift method of Decimator objects, with positive shift for string float constructor args
        """
        print('f\nIn test_14_shift_positive_string_float')
        print('--------------------------')
        shifts = [0,1,2,3,10,20]
        for decimator in float_string_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                print(f'Fraction precision: {shifted_decimator.fraction_precision}')
                self.assertTrue( abs(difference) < 10 ** ( (-1)*(shifted_decimator.fraction_precision-1) ) )


    def test_15_shift_negative_string_float(self):
        """
        Test shift method of Decimator objects, with negative shift for string float constructor args
        """
        print('f\nIn test_15_shift_negative_string_float')
        print('--------------------------')
        shifts = [-1,-2,-3,-10,-20]
        for decimator in float_string_decimators:
            for shift in shifts:
                print()
                print(f'Decimator number: {decimator.number}')
                print(f'Decimator positive_decimals: {decimator.positive_decimals}')
                print(f'Decimator negative_decimals: {decimator.negative_decimals}')
                print(f'Shift: {shift}')
                string = str(decimator)
                shifted_decimator = decimator.shift(shift)
                print(f'Shifted decimator: {str(shifted_decimator)}')
                value_a = decimator.get_value()*10**shift
                value_b = shifted_decimator.get_value()
                difference = abs(value_a - value_b)
                print(f'Value A: {str(value_a)}')
                print(f'Value B: {str(value_b)}')
                try:
                    self.assertEqual(decimator.get_value() * 10 ** shift, shifted_decimator.get_value())
                except AssertionError as error:
                    try:
                        self.assertTrue(abs(difference) < 10 ** shift-decimator.fraction_precision)
                    except AssertionError as error:
                        self.assertTrue(abs(difference) < 10 ** decimator.fraction_precision)



if __name__ == '__main__':
    unittest.main()

