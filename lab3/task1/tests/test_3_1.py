import unittest
import datetime
import time
import tracemalloc

from lab3.task1.src.task1_1 import randomized_quick_sort as sort_1
from lab3.task1.src.task1_2 import randomized_quick_sort as sort_2
from lab3.task1.src.task1_1 import to_sort


class TestQuickSort(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        unsorted_list = [2, 3, 9, 2, 2]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 2, 2, 3, 9]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = sort_1(unsorted_list, 0, len(unsorted_list) - 1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_sort_given_list(self):
        # Given
        unsorted_list = [2, 3, 9, 2, 2]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 2, 2, 3, 9]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = sort_2(unsorted_list, 0, len(unsorted_list) - 1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = [1, 5, 24, 34, 374, 1000]
        data = [1, 24, 5, 34, 1000, 374]
        expected_time = 2
        expected_memory = 256
        n = 6

        # when
        time_st = time.perf_counter()
        result = to_sort(n, data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = to_sort(n, data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
