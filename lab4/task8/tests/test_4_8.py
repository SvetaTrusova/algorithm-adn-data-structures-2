import unittest
import datetime
import time
import tracemalloc

from lab4.task8.src.task8 import postfix_calculate


class TestPostfixCalculate(unittest.TestCase):
    def test1_should_postfix_calculate(self):
        # Given
        commands = '8 9 + 1 7 - *'
        expected_time = datetime.timedelta(2)
        expected_result = -102

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = postfix_calculate(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_postfix_calculate(self):
        # Given
        commands = '8 9 +'
        expected_time = datetime.timedelta(2)
        expected_result = 17

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = postfix_calculate(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # given
        commands = '8 9 + 1 7 - *'
        expected_result = -102
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = postfix_calculate(commands)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = postfix_calculate(commands)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time,
                             f"Затрачено {time_end} секунд, превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Затрачено {memory} MB, превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()