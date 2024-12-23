import unittest
import tracemalloc
import time
import datetime
from lab3.task4.src.task4 import count_intervals


class TestIntervalsCount(unittest.TestCase):
    def test1_should_count_given_list(self):
        # Given
        s, p = 2, 3
        given_intervals = [[0, 5], [7, 10]]
        given_dots = [1, 6, 11]
        expected_time = datetime.timedelta(2)
        expected_result = [1, 0, 0]

        # When
        start_time = datetime.datetime.now()
        result = count_intervals(p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_count_given_list(self):
        # Given
        s, p = 1, 3
        given_intervals = [[-10, 10]]
        given_dots = [-100, 100, 0]
        expected_time = datetime.timedelta(2)
        expected_result = [0, 0, 1]

        # When
        start_time = datetime.datetime.now()
        result = count_intervals(p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_count_given_list(self):
        # Given
        s, p = 3, 2
        given_intervals = [[0, 5], [-3, 2], [7, 10]]
        given_dots = [1, 6]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 0]

        # When
        start_time = datetime.datetime.now()
        result = count_intervals(p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # given
        s, p = 3, 2
        intervals = [[0, 5], [-3, 2], [7, 10]]
        dots = [1, 6]
        expected_result = [2, 0]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = count_intervals(p, intervals, dots)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = count_intervals(p, intervals, dots)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
