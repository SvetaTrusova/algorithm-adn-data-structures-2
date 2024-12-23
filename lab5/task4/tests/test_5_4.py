import unittest
import tracemalloc
import time
from lab5.task4.src.task4 import min_heapify, build_min_heap


class TestMinHeapFunctions(unittest.TestCase):

    def test_min_heapify(self):
        arr = [5, 3, 8, 1, 2, 7]
        swaps = []
        min_heapify(arr, len(arr), 0, swaps)
        self.assertEqual(arr, [3, 1, 8, 5, 2, 7])

    def test_build_min_heap(self):
        arr = [5, 4, 3, 2, 1]
        expected_swaps = [(1, 4), (0, 1), (1, 3)]
        swaps = build_min_heap(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 4])
        self.assertEqual(swaps, expected_swaps)

    def test_single_element(self):
        arr = [10]
        swaps = build_min_heap(arr)
        self.assertEqual(arr, [10])
        self.assertEqual(swaps, [])

    def test_empty_array(self):
        arr = []
        swaps = build_min_heap(arr)
        self.assertEqual(arr, [])
        self.assertEqual(swaps, [])

    def test_already_heap(self):
        arr = [1, 2, 3, 4, 5, 6]
        swaps = build_min_heap(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])
        self.assertEqual(swaps, [])

    def test_large_values(self):
        arr = [10**9, 10**8, 10**7, 10**6, 10**5]
        swaps = build_min_heap(arr)
        self.assertEqual(arr[0], 10**5)
        self.assertTrue(all(arr[i] <= arr[2*i+1] and arr[i] <= arr[2*i+2] for i in range(len(arr)//2)))

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = []
        data = [-1, 0, 4, 0, 3]
        n = 5
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = build_min_heap(data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
