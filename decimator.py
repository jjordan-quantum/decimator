class Decimator:
    def __init__(self, number):
        assert isinstance(number, int) or isinstance(number, float) or self._is_number(number), 'number must be int or float'
        self.number = number
        self.positive_decimals = []
        self.negative_decimals = []
        self._set()

    def _set(self):
        if isinstance(self.number, int):
            assert self.number >= 0, 'number must not be negative'
            self.number_string = str(self.number)
            self.integer_string = self.number_string
            self.fraction_string = False
            self.fraction_precision = 0
        elif isinstance(self.number, float):
            assert self.number >= 0, 'number must not be negative'
            self.number_string = str(self.number)
            n = self.number_string.find('.')
            self.integer_string = self.number_string[0:n]
            self.fraction_string = '0' + self.number_string[n:]
            self.fraction_precision = len(self.fraction_string) - 2
        elif isinstance(self.number, str):
            assert '-' not in self.number, 'number must not be negative'
            self.number_string = self.number
            if '.' in self.number:
                n = self.number_string.find('.')
                self.integer_string = self.number_string[0:n]
                self.fraction_string = '0' + self.number_string[n:]
                self.fraction_precision = len(self.fraction_string) - 2
                pass
            else:
                self.integer_string = self.number_string
                self.fraction_precision = 0
                self.fraction_string = False
        self._get_positive_decimals_from_string(self.integer_string)
        self._get_negative_decimals_from_string(self.fraction_string)

    def _is_number(self, number):
        if '.' in number:
            try:
                cast = float(number)
            except:
                return False
        else:
            try:
                integer_cast = int(number)
            except:
                return False
        return True

    def _get_positive_decimals_from_string(self, integer):
        index = len(integer)-1
        while index >= 0:
            value = self._get_digit_at_index(integer, index)
            self.positive_decimals.append(value)
            index -= 1

    def _get_digit_at_index(self, number, index):
        try:
            value = number[index]
            return int(value)
        except:
            return '0'

    def _get_negative_decimals_from_string(self, fraction):
        if not fraction:
            self.negative_decimals.append(0)
            return

        index = 0
        while index < self.fraction_precision:
            value = self._get_digit_at_index(fraction, index+2)
            self.negative_decimals.append(value)
            index +=1

    def add(self, number):
        pass

    def sub(self, number):
        pass

    def mul(self, number):
        pass

    def div(self, number):
        pass

    def pow(self, number):
        pass

    def shift(self, shift):
        assert isinstance(shift, int), 'shift must be int'
        decimator = Decimator(self.number)
        decimator._shift(shift)
        decimator._update_strings()
        return decimator

    def _update_strings(self):
        self.integer_string = self._get_integer_string()
        self._check_for_zero_fraction()
        self.fraction_string = '0'+self._get_fraction_string()
        self._update_fraction_precision()

    def _check_for_zero_fraction(self):
        if self.get_fractional_value() == 0.0:
            self.negative_decimals = [0]

    def _update_fraction_precision(self):
        if self.negative_decimals == [0]:
            self.fraction_precision = 0
        else:
            self.fraction_precision = len(self.negative_decimals)

    def _shift(self, shift):
        if shift > 0:
            self._shift_positive(shift)
        if shift < 0:
            self._shift_negative(shift)

    def _shift_positive(self, shift):
        while shift > 0:
            popped_value = self._pop_negative()
            self._insert_positive(popped_value)
            shift -= 1

    def _shift_negative(self, shift):
        while shift < 0:
            popped_value = self._pop_positive()
            self._insert_negative(popped_value)
            shift += 1

    def _insert_positive(self, value):
        self.positive_decimals.insert(0, value)

    def _insert_negative(self, value):
        self.negative_decimals.insert(0, value)

    def _pop_positive(self):
        if len(self.positive_decimals) == 1:
            pop = self.positive_decimals.pop(0)
            self.positive_decimals.append(0)
            return pop
        return self.positive_decimals.pop(0)

    def _pop_negative(self):
        if len(self.negative_decimals) == 0:
            return 0
        return self.negative_decimals.pop(0)

    def __str__(self):
        number = self._get_integer_string()
        if self.fraction_string:
            number = number + self._get_fraction_string()
        return number

    def _get_integer_string(self):
        integer = ''
        for decimal in self.positive_decimals:
            integer = str(decimal) + integer
        return integer

    def _get_fraction_string(self):
        fraction = ''
        fraction = fraction + '.'
        if len(self.negative_decimals) > 0:
            for decimal in self.negative_decimals:
                fraction = fraction + str(decimal)
        else:
            fraction = fraction + '0'
        return fraction

    ##########################################
    #DO NEXT

    def round(self, digits):
        assert isinstance(digits, int), 'digits must be int'
        assert digits >= 0, 'digits must be greater than or equal to'
        decimator = Decimator(self.number)
        return decimator

    def _strip(self, digits):
        if len(self.negative_decimals) > digits:
            self.negative_decimals = self.negative_decimals[0:digits]

    def get_value(self):
        # I have found that the maximum floating point precision that can be trusted is 16
        return float(self.__str__())

    def get_integer_value(self):
        value = 0
        for i in range(len(self.positive_decimals)):
            value += self.positive_decimals[i] * (10 ** i)
        return value

    def get_fractional_value(self):
        value = 0.0
        for i in range(len(self.negative_decimals)):
            value += self.negative_decimals[i] * (10 ** ((-1)*(i+1)))
        return value


