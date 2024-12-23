import unittest
import time
import tracemalloc
from lab3.task3.src.task3 import pugalo_sort


class TestMatreshkaSorting(unittest.TestCase):

    def test_should_sort_with_k(self):
        # Given
        n = 5
        k = 3
        arr = [1, 5, 3, 4, 1]
        expected_result = "ДА"

        # When
        result = pugalo_sort(n, k, arr)

        # Then
        self.assertEqual(result, expected_result)

    def test_should_not_sort_with_k(self):
        # Given
        n = 3
        k = 2
        arr = [2, 1, 3]
        expected_result = "НЕТ"

        # When
        result = pugalo_sort(n, k, arr)

        # Then
        self.assertEqual(result, expected_result)

    def test_should_check_used_memory_and_time(self):
        # Given
        expected_result = "НЕТ"
        data = [1, 24, 5, 34, 1000, 374]
        n = 6
        k = 3
        expected_time = 2
        expected_memory = 256

        # When
        time_st = time.perf_counter()
        result = pugalo_sort(n, k, data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = pugalo_sort(n, k, data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Convert to MB
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
