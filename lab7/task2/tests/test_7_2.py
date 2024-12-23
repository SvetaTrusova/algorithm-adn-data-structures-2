import unittest
from lab7.task2.src.task2 import find_min_operations


class TestFindMinOperations(unittest.TestCase):

    def test_case_2(self):
        # given
        n = 2

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '1\n')
        self.assertEqual(result[1], '1 2')

    def test_case_3(self):
        # given
        n = 3

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '1\n')
        self.assertEqual(result[1], '1 3')

    def test_case_4(self):
        # given
        n = 4

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '2\n')
        self.assertEqual(result[1], '1 2 4')

    def test_case_5(self):
        # given
        n = 5

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '3\n')
        self.assertEqual(result[1], '1 2 4 5')

    def test_case_6(self):
        # given
        n = 10

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '3\n')
        self.assertEqual(result[1], '1 3 9 10')

    def test_case_7(self):
        # given
        n = 15

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '4\n')
        self.assertEqual(result[1], '1 2 4 5 15')

    def test_case_8(self):
        # given
        n = 100

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '7\n')
        self.assertEqual(result[1], '1 2 4 8 24 25 50 100')

    def test_case_9(self):
        # given
        n = 9

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '2\n')
        self.assertEqual(result[1], '1 3 9')

    def test_case_10(self):
        # given
        n = 6

        # when
        result = find_min_operations(n)

        # then
        self.assertEqual(result[0], '2\n')
        self.assertEqual(result[1], '1 2 6')


if __name__ == '__main__':
    unittest.main()
