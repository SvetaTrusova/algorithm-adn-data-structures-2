from lab2.task1.src.task1 import to_sort, merge_sort
import time
import tracemalloc
import unittest


class TestMergeSort(unittest.TestCase):
    def test_should_check_insertion_sort(self):
        """Проверка сортировки слиянием"""

        # given
        data = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        exepted_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # when
        sorted_arr = merge_sort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_check_single_element(self):
        """Тест на список из одного элемента"""
        # given
        data = [42]
        exepted_data = [42]

        # when
        sorted_arr = merge_sort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_check_sorted_list(self):
        """Тест на уже отсортированный список"""
        # given
        data = [1, 2, 3, 4, 5]
        exepted_data = [1, 2, 3, 4, 5]

        # when
        sorted_arr = merge_sort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_check_reverse_order(self):
        """Тест на список в обратном порядке"""
        # given
        data = [5, 4, 3, 2, 1]
        exepted_data = [1, 2, 3, 4, 5]

        # when
        sorted_arr = merge_sort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_check_all_equal_elements(self):
        """Тест на список с одинаковыми элементами"""
        # given
        data = [7, 7, 7, 7, 7]
        exepted_data = [7, 7, 7, 7, 7]

        # when
        sorted_arr = merge_sort(data)

        # then
        self.assertEqual(sorted_arr, exepted_data)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = '1 5 24 34 374 1000'
        data = [1, 24, 5, 34, 1000, 374]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = to_sort(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = to_sort(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
