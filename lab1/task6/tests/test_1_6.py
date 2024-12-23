from lab1.utils import bubblesort
from lab1.task6.src.task6 import to_sort
import time
import unittest


class TestBubbleSort(unittest.TestCase):
    def test_should_single_element(self):
        """Проверка на список с одним элементом."""

        # given
        n = 1
        data = [42]
        expected_result = [42]

        # when
        sorted_data = bubblesort(n, data)

        # then
        self.assertEqual(sorted_data, expected_result)

    def test_should_sorted_ascending(self):
        """Проверка на уже отсортированный список по возрастанию."""

        # given
        n = 5
        data = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        # when
        sorted_data = bubblesort(n, data)

        # then
        self.assertEqual(sorted_data, expected_result)

    def test_should_sorted_descending(self):
        """Проверка на список, отсортированный по убыванию."""

        # given
        n = 5
        data = [5, 4, 3, 2, 1]
        exepted_result = [1, 2, 3, 4, 5]

        # when
        sorted_data = bubblesort(n, data)

        # then
        self.assertEqual(sorted_data, exepted_result)

    def test_should_check_functions(self):
        # given
        expected_result = '4 5 100 245 374 10120'
        data = [10120, 245, 5, 4, 100, 374]
        n = 6
        expected_time = 2

        # when
        time_st = time.perf_counter()
        result = to_sort(n, data)
        time_end = time.perf_counter() - time_st

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
