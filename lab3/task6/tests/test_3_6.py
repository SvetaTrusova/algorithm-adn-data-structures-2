import unittest
import tracemalloc
import time
import datetime

from lab3.task6.src.task6 import sum_of_every_tenth_element


class TestSumOfEveryTenthElement(unittest.TestCase):

    def test1_should_calculate_sum_correctly(self):
        # Given
        a = [7, 1, 4, 9]
        b = [2, 7, 8, 11]
        expected_time = datetime.timedelta(2)
        expected_result = 51  # Ожидаемый результат для данного теста

        # When
        start_time = datetime.datetime.now()
        result = sum_of_every_tenth_element(a, b)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_calculate_sum_correctly(self):
        # Given
        a = [1, 2]
        b = [3, 4]
        expected_time = datetime.timedelta(2)
        expected_result = 3  # Ожидаемый результат для данного теста

        # When
        start_time = datetime.datetime.now()
        result = sum_of_every_tenth_element(a, b)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_calculate_sum_correctly(self):
        # Given
        a = [5, 10]
        b = [3, 6]
        expected_time = datetime.timedelta(2)
        expected_result = 15  # Ожидаемый результат для данного теста

        # When
        start_time = datetime.datetime.now()
        result = sum_of_every_tenth_element(a, b)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # Given
        a = [7, 1, 4, 9]
        b = [2, 7, 8, 11]
        expected_result = 51
        expected_time = 2
        expected_memory = 256

        # When
        time_st = time.perf_counter()
        result = sum_of_every_tenth_element(a, b)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = sum_of_every_tenth_element(a, b)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
