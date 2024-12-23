import unittest
import tracemalloc
import time
from lab6.task6.src.task6 import is_fibonacci_number, fibonacci_check

class TestFibonacciCheck(unittest.TestCase):

    def test_single_fibonacci_number(self):
        # Given
        arr = [5]
        expected = ["Yes"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_single_non_fibonacci_number(self):
        # Given
        arr = [6]
        expected = ["No"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_numbers_mixed(self):
        # Given
        arr = [5, 6, 8, 13, 22]
        expected = ["Yes", "No", "Yes", "Yes", "No"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_large_fibonacci_number(self):
        # Given
        arr = [832040]
        expected = ["Yes"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_large_non_fibonacci_number(self):
        # Given
        arr = [1000000]
        expected = ["No"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_fibonacci_numbers(self):
        # Given
        arr = [5, 13, 21, 34]
        expected = ["Yes", "Yes", "Yes", "Yes"]

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_large_range(self):
        # Given
        arr = list(range(1, 11))
        expected = ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No']

        # When
        result = fibonacci_check(arr)

        # Then
        self.assertEqual(result, expected)

    def test_should_check_used_memory_and_time(self):
        # given
        expected = ["Yes", "No", "Yes", "Yes", "No"]
        candidates_input = [5, 6, 8, 13, 22]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = fibonacci_check(candidates_input)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()

