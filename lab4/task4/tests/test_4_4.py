import unittest
import datetime
import time
import tracemalloc
from lab4.task4.src.task4 import check_brackets


class TestCheckBrackets(unittest.TestCase):
    def test1_should_check_brackets(self):
            # Given
            brackets_given = '[]'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_scheck_brackets(self):
        # Given
        brackets_given = '{}[]'
        expected_time = datetime.timedelta(5)
        expected_result = 'Success'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = check_brackets(brackets_given)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_check_brackets(self):
        # Given
        brackets_given = '[()]'
        expected_time = datetime.timedelta(5)
        expected_result = 'Success'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = check_brackets(brackets_given)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test4_should_check_brackets(self):
        # Given
        brackets_given = '(())'
        expected_time = datetime.timedelta(5)
        expected_result = 'Success'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = check_brackets(brackets_given)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test5_should_check_brackets(self):
        # Given
        brackets_given = '{'
        expected_time = datetime.timedelta(5)
        expected_result = 1

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = check_brackets(brackets_given)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # given
        commands = 'foo(bar[i);'
        expected_result = 'Success'
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = check_brackets([commands])
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = check_brackets([commands])
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time,
                             f"Затрачено {time_end} секунд, превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Затрачено {memory} MB, превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
