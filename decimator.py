class Decimator:
    def __init__(self, number):
        assert isinstance(number, int) or isinstance(number, float), 'number must be int or float'
        assert number >= 0, 'number must not be negative'
        self.number = number
        self.positive_decimals = []
        self.negative_decimals = []
        self._set()

    def _set(self):
        if isinstance(self.number, int):
            self.integer_string = str(self.number)
            self.fraction_string = False
            self._get_positive_decimals_from_string(self.integer_string)
            self.fraction_precision = 0
        elif isinstance(self.number, float):
            self.integer_string = str(int(self.number))
            self.fraction_string = str(self.number - int(self.number))
            self._get_positive_decimals_from_string(self.integer_string)
            self.fraction_precision = len(self.fraction_string) - 2
            self._get_negative_decimals_from_string(self.fraction_string)
        elif isinstance(self.number, str):
            assert self._is_number(self.number), 'string must contain only int or float'
            if '.' in self.number:
                n = number.find('.')
                self.integer_string = self.number[0:n]
                self.fraction_string = self.number[n+1:]
                self._get_positive_decimals_from_string(self.integer_string)
                self.fraction_precision = len(self.fracton_string) - 2
                self._get_negative_decimals_from_string(self.fraction_string)
                pass
            else:
                self._get_positive_decimals_from_string(self.number)
                self.fraction_precision = 0

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
            return 0

    def _get_negative_decimals_from_string(self, fraction):
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
        assert isinstance(number, int), 'shift must be int'
        decimator = Decimator(self.number)
        decimator._shift(shift)
        return decimator

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
        if len(self.positive_decimals) == 0:
            return 0
        return self.positive_decimals.pop(0)

    def _pop_negative(self):
        if len(self.negative_decimals) == 0:
            return 0
        return self.negative_decimals.pop(0)

    def __str__(self):
        number = ''
        for decimal in self.positive_decimals:
            number = str(decimal) + number
        if self.fraction_string:
            number = number + '.'
            for decimal in self.negative_decimals:
                number = number + str(decimal)
        return number

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
        return self.get_integer_value() + self.get_fractional_value()

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


