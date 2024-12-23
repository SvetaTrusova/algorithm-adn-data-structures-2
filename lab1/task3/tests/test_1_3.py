from lab1.utils import insertionsort_not_increasing
from lab1.task3.src.task3 import to_sort
import time
import unittest


class TestInsertionSortNotIncrease(unittest.TestCase):
    def test_should_single_element(self):
        # given
        data = [42]
        exepted_result = [42]

        # when
        sorted_data = insertionsort_not_increasing(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_all_elements_equal(self):
        # given
        data = [5, 5, 5, 5]
        exepted_result = [5, 5, 5, 5]

        # when
        sorted_data = insertionsort_not_increasing(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_already_sorted_descending(self):
        # given
        data = [9, 7, 5, 3, 1]
        exepted_result = [9, 7, 5, 3, 1]

        # when
        sorted_data = insertionsort_not_increasing(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_sorted_ascending(self):
        # given
        data = [1, 3, 5, 7, 9]
        exepted_result = [9, 7, 5, 3, 1]

        # when
        sorted_data = insertionsort_not_increasing(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_check_functions(self):
        # given
        expected_result = '1000 374 34 24 5 1'
        data = [1, 24, 5, 34, 1000, 374]
        n = 6
        expected_time = 2

        # when
        time_st = time.perf_counter()
        result = to_sort(data)
        time_end = time.perf_counter() - time_st

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
