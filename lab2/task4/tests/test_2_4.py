from lab2.task4.src.task4 import binary_search
import time
import tracemalloc
import unittest


class TestInversions(unittest.TestCase):
    def test_should_check_existing_number(self):
        # given
        arr = [1, 3, 5, 7, 9, 11]

        # when
        result = binary_search(arr, 7)

        # then
        self.assertEqual(result, 3)  # Индекс числа 7 в массиве - 3

    def test_should_check_first_element(self):
        # given
        arr = [1, 3, 5, 7, 9, 11]

        # when
        result = binary_search(arr, 1)

        # then
        self.assertEqual(result, 0)  # Индекс числа 1 в массиве - 0

    def test_should_check_last_element(self):
        # given
        arr = [1, 3, 5, 7, 9, 11]

        # when
        result = binary_search(arr, 11)

        # then
        self.assertEqual(result, 5)  # Индекс числа 11 в массиве - 5

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = 3
        data = [1, 5, 24, 34, 374, 1000]
        target = 34
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = binary_search(data, target)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()

