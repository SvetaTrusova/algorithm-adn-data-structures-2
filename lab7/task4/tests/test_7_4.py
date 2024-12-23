import unittest
import datetime

from lab7.task4.src.task4 import longest_common_subsequence


class TestCcommonSubsequence(unittest.TestCase):
    def test1_should_find_longest_common_subsequence(self):
        # Given
        n, m = 3, 2
        a_list = [2, 7, 5]
        b_list = [2, 5]
        expected_time = datetime.timedelta(1)
        expected_result = 2

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = longest_common_subsequence(n, m, a_list, b_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_find_longest_common_subsequence(self):
        # Given
        n, m = 1, 4
        a_list = [7]
        b_list = [1, 2, 3, 4]
        expected_time = datetime.timedelta(1)
        expected_result = 0

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = longest_common_subsequence(n, m, a_list, b_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_find_longest_common_subsequence(self):
        # Given
        n, m = 4, 4
        a_list = [2, 7, 8, 3]
        b_list = [5, 2, 8, 7]
        expected_time = datetime.timedelta(1)
        expected_result = 2

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = longest_common_subsequence(n, m, a_list, b_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()