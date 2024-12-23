#
from lab2.task10.src.task10 import merge_sort
import unittest
import time
import tracemalloc


class TestMergeSort(unittest.TestCase):

    def test_should_check_merge_sort_sorted(self):
        # given
        list_arr = [1, 2, 3, 4, 5]
        result = merge_sort(list_arr)

        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_should_check_merge_sort_reverse(self):
        # given
        list_arr = [5, 4, 3, 2, 1]
        result = merge_sort(list_arr)

        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_should_check_merge_sort_unsorted(self):
        # given
        list_arr = [3, 1, 4, 5, 2]
        result = merge_sort(list_arr)

        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_should_check_merge_sort_empty(self):
        # given
        list_arr = []
        result = merge_sort(list_arr)

        # then
        self.assertEqual(result, [])

    def test_should_check_merge_sort_single_element(self):
        # given
        list_arr = [1]
        result = merge_sort(list_arr)

        # then
        self.assertEqual(result, [1])

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = [1, 5, 24, 34, 374, 1000]
        data = [1, 34, 5, 24, 1000, 374]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = merge_sort(data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
