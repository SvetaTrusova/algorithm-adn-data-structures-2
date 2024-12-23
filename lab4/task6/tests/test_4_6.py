import unittest
import datetime
import time
import tracemalloc
from lab4.task6.src.task6 import queue_min


class TestQueue(unittest.TestCase):
    def test_should_queue(self):
        # Given
        commands = ['+ 1', '?', '+ 10', '?', '-', '?', '-']
        expected_time = datetime.timedelta(2)
        expected_result = [1, 1, 10]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = queue_min(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_used_memory_and_time(self):
        # given
        commands = ['+ 1', '?', '+ 10', '?', '-', '?', '-']
        expected_result = [1, 1, 10]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = queue_min(commands)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = queue_min(commands)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time,
                             f"Затрачено {time_end} секунд, превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Затрачено {memory} MB, превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()