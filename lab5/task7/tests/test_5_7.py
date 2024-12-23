import unittest
import time
import tracemalloc
from lab5.task7.src.task7 import max_heapify, heap_sort


class TestHeapSort(unittest.TestCase):

    def test_max_heapify_basic(self):
        # given
        arr = [3, 5, 1, 2, 4]

        # when
        max_heapify(arr, 5, 0)

        # then
        self.assertEqual(arr, [5, 4, 1, 2, 3])

    def test_heap_sort(self):
        # given
        arr = [3, 5, 1, 2, 4]

        # when
        sorted_arr = heap_sort(arr)

        # then
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_heap_sort_single_element(self):
        # given
        arr = [10]

        # when
        sorted_arr = heap_sort(arr)

        # then
        self.assertEqual(sorted_arr, [10])

    def test_heap_sort_sorted_descending(self):
        # given
        arr = [10, 8, 6, 4, 2]

        # when
        sorted_arr = heap_sort(arr)

        # then
        self.assertEqual(sorted_arr, [2, 4, 6, 8, 10])

    def test_heap_sort_sorted_ascending(self):
        # given
        arr = [1, 2, 3, 4, 5]

        # when
        sorted_arr = heap_sort(arr)

        # then
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_large_input(self):
        # given
        arr = list(range(1, 10001))

        # when
        sorted_arr = heap_sort(arr)

        # then
        self.assertEqual(sorted_arr, list(range(1, 10001)))

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = [1, 5, 24, 34, 374, 1000]
        data = [1, 24, 5, 34, 1000, 374]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = heap_sort(data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
