import unittest
import tracemalloc
import time
import datetime
from lab3.task5.src.task5 import h_index


class TestHIndex(unittest.TestCase):

    def test1_should_calculate_h_index_correctly(self):
        # Given
        citations = [6, 5, 3, 1, 0]
        expected_time = datetime.timedelta(2)
        expected_result = 3

        # When
        start_time = datetime.datetime.now()
        result = h_index(citations)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_calculate_h_index_correctly(self):
        # Given
        citations = [4, 3, 2, 1, 0]
        expected_time = datetime.timedelta(2)
        expected_result = 2  # Индекс Хирша для данного списка должен быть 2

        # When
        start_time = datetime.datetime.now()
        result = h_index(citations)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_calculate_h_index_correctly(self):
        # Given
        citations = [1, 0, 0]
        expected_time = datetime.timedelta(2)
        expected_result = 1  # Индекс Хирша для данного списка должен быть 1

        # When
        start_time = datetime.datetime.now()
        result = h_index(citations)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test4_should_calculate_h_index_correctly(self):
        # Given
        citations = [10, 8, 5, 3, 1]
        expected_time = datetime.timedelta(2)
        expected_result = 3  # Индекс Хирша для данного списка должен быть 4

        # When
        start_time = datetime.datetime.now()
        result = h_index(citations)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # Given
        citations = [6, 5, 3, 1, 0]
        expected_result = 3
        expected_time = 2
        expected_memory = 256

        # When
        time_st = time.perf_counter()
        result = h_index(citations)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = h_index(citations)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
