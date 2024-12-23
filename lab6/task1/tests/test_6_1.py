import unittest
import tracemalloc
import time
from lab6.task1.src.task1 import fibonacci_check


class TestFibonacciCheck(unittest.TestCase):

    def test_add_and_check(self):
        # Given
        n = 3
        data = ['A 2', 'A 5', '? 2']
        expected = ['Y']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_add_remove_and_check(self):
        # Given
        n = 4
        data = ['A 2', 'A 5', 'D 2', '? 2']
        expected = ['N']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_operations(self):
        # Given
        n = 6
        data = ['A 10', 'A 20', 'A 30', '? 20', 'D 10', '? 10', '? 30']
        expected = ['Y', 'N']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_check_nonexistent_element(self):
        # Given
        n = 2
        data = ['A 100', '? 200']
        expected = ['N']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_add_and_check_multiple(self):
        # Given
        n = 5
        data = ['A 100', 'A 200', '? 100', '? 200', '? 300']
        expected = ['Y', 'Y', 'N']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_empty_operations(self):
        # Given
        n = 1
        data = ['? 1']
        expected = ['N']

        # When
        result = fibonacci_check(n, data)

        # Then
        self.assertEqual(result, expected)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = ['N']
        data = ['A 100', '? 200']
        n = 2
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = fibonacci_check(n, data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
