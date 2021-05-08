from src.main.python import constant as constants


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


# https://oeis.org/A006968/a006968.txt


if __name__ == "__main__":
    while True:
        print("Please enter arabic numeral between 0 and 3999 and press enter. Enter 0 to exit.")
        arabic_number = input()
        if arabic_number.strip() == '0':
            break
        if arabic_number.strip().isnumeric() and int(arabic_number) in range(constants.MIN_ROMAN, constants.MAX_ROMAN):
            print(NumberConverter.get_result(int(arabic_number.strip())))
        else:
            print("Invalid number.")
