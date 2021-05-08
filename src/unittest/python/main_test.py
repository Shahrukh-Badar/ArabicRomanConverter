import unittest
import csv
from src.main.python.main import NumberConverter


class TestNumberConverter(unittest.TestCase):

    def test_get_result(self):
        test_data = {}
        with open('../../../test.csv', newline='') as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=',')
            for row in spam_reader:
                if row and len(row) == 2:
                    test_data[int(row[0].strip())] = row[1].strip()

        for i in range(1, 4000):
            res = NumberConverter.get_result(i)
            self.assertEqual(res, test_data[i])


if __name__ == '__main__':
    unittest.main()
