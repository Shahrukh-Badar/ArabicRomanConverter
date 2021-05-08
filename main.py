import constant as constants


class NumberConverter():

    @staticmethod
    def get_result(arabic_number):
        arabic_number = str(arabic_number)
        units, tens, hundreds, thousands = constants.EMPTY_STRING, constants.EMPTY_STRING, constants.EMPTY_STRING, constants.EMPTY_STRING
        if len(arabic_number) == 4:
            thousands = NumberConverter.arabic_to_roman_converter(int(arabic_number[0]), constants.THOUSAND)
            hundreds = NumberConverter.arabic_to_roman_converter(int(arabic_number[1]), constants.HUNDRED)
            tens = NumberConverter.arabic_to_roman_converter(int(arabic_number[2]), constants.TEN)
            units = NumberConverter.arabic_to_roman_converter(int(arabic_number[3]), constants.ONE)
        if len(arabic_number) == 3:
            hundreds = NumberConverter.arabic_to_roman_converter(int(arabic_number[0]), constants.HUNDRED)
            tens = NumberConverter.arabic_to_roman_converter(int(arabic_number[1]), constants.TEN)
            units = NumberConverter.arabic_to_roman_converter(int(arabic_number[2]), constants.ONE)
        if len(arabic_number) == 2:
            tens = NumberConverter.arabic_to_roman_converter(int(arabic_number[0]), constants.TEN)
            units = NumberConverter.arabic_to_roman_converter(int(arabic_number[1]), constants.ONE)
        elif len(arabic_number) == 1:
            units = NumberConverter.arabic_to_roman_converter(int(arabic_number[0]), constants.ONE)

        return thousands + hundreds + tens + units

    @staticmethod
    def arabic_to_roman_converter(number, digit_place=constants.ONE):
        number = int(number)
        if number == constants.ZERO:
            return constants.EMPTY_STRING
        roman_numeral = constants.EMPTY_STRING
        one, three, four, five, eight, nine, ten = 1 * digit_place, \
                                                   3 * digit_place, 4 * digit_place, 5 * digit_place, \
                                                   8 * digit_place, 9 * digit_place, 10 * digit_place

        if digit_place == constants.TEN:
            number = number * digit_place
        elif digit_place == constants.HUNDRED:
            number = number * digit_place
        elif digit_place == constants.THOUSAND:
            number = number * digit_place

        if number in constants.META_DATA.keys():
            return constants.META_DATA[number]
        elif number <= three:
            roman_numeral = constants.META_DATA[one] * int(number / digit_place)
        elif number == four:
            roman_numeral = constants.META_DATA[one] + constants.META_DATA[five]
        elif number > five and number <= eight:
            roman_numeral = constants.META_DATA[five] + (
                    constants.META_DATA[one] * (int(number / digit_place) - int(five / digit_place)))
        elif number == nine:
            roman_numeral = constants.META_DATA[one] + constants.META_DATA[ten]
        return roman_numeral

    @staticmethod
    def validate_input(arabic_number):
        in_valid_range = lambda num: int(num) in range(constants.MIN_ROMAN, constants.MAX_ROMAN)
        if type(arabic_number) == int and in_valid_range(arabic_number):
            return True
        elif type(arabic_number) == str and arabic_number.strip().isnumeric() and in_valid_range(int(arabic_number)):
            return True
        else:
            return False


if __name__ == "__main__":
    arabic_number = 3999
    if NumberConverter.validate_input(arabic_number):
        print(NumberConverter.get_result(arabic_number))
    else:
        print('Invalid Input.')
