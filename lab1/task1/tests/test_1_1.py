from lab1.utils import insertionsort, memory_usage_process
from lab1.task1.src.task1 import to_sort
import time
import unittest


class TestInsertionSort(unittest.TestCase):
    def test_should_insertion_sort(self):
        """Проверка сортировки вставками"""
        # given
        data = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        exepted_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # when
        sorted_arr = insertionsort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_single_element(self):
        """Тест на список из одного элемента"""
        # given
        data = [42]
        exepted_data = [42]

        # when
        sorted_arr = insertionsort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_sorted_list(self):
        """Тест на уже отсортированный список"""
        # given
        data = [1, 2, 3, 4, 5]
        exepted_data = [1, 2, 3, 4, 5]

        # when
        sorted_arr = insertionsort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_reverse_order(self):
        """Тест на список в обратном порядке"""
        # given
        data = [5, 4, 3, 2, 1]
        exepted_data = [1, 2, 3, 4, 5]

        # when
        sorted_arr = insertionsort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_all_equal_elements(self):
        """Тест на список с одинаковыми элементами"""
        # given
        data = [7, 7, 7, 7, 7]
        exepted_data = [7, 7, 7, 7, 7]

        # when
        sorted_arr = insertionsort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_should_check_functions(self):
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


if __name__ == "__main__":
    unittest.main()
