from lab1.utils import selectionsort
from lab1.task5.src.task5 import to_sort
import time
import unittest


class TestSelectionSort(unittest.TestCase):
    def test_should_single_element(self):
        # given
        data = [42]
        exepted_result = [42]

        # when
        sorted_data = selectionsort(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_all_elements_equal(self):
        # given
        data = [5, 5, 5, 5]
        exepted_result = [5, 5, 5, 5]

        # when
        sorted_data = selectionsort(data)
        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_already_sorted_ascending(self):
        # given
        data = [1, 2, 3, 4, 5]
        exepted_result = [1, 2, 3, 4, 5]

        # when
        sorted_data = selectionsort(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_sorted_descending(self):
        #given
        data = [5, 4, 3, 2, 1]
        exepted_result = [1, 2, 3, 4, 5]

        # when
        sorted_data = selectionsort(data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_check_functions(self):
        # given
        expected_result = '1 5 24 34 374 1000'
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


if __name__ == '__main__':
    unittest.main()
