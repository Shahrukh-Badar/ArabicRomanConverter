import unittest
import csv
from main import NumberConverter
import constant as constants


class TestNumberConverter(unittest.TestCase):

    def test_get_result(self):
        test_data = {}
        ## https://oeis.org/A006968/a006968.txt
        with open(constants.TEST_FILE_NAME, newline=constants.EMPTY_STRING) as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=constants.DELIMETER)
            for row in spam_reader:
                if row and len(row) == 2:
                    test_data[int(row[0].strip())] = row[1].strip()

        for i in range(constants.MIN_ROMAN, constants.MAX_ROMAN):
            res = NumberConverter.get_result(i)
            self.assertEqual(res, test_data[i])


if __name__ == '__main__':
    unittest.main()
