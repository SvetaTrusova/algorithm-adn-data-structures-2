import unittest
import time
import tracemalloc
from lab4.task2.src.task2 import process_queue


# Тестовая оболочка
class TestProcessQueue(unittest.TestCase):

    def test_process_queue_basic(self):
        # given
        commands = ["+ 1", "+ 2", "-", "+ 3", "-"]
        expected_result = [1, 2]

        # when
        result = process_queue([commands])

        # then
        self.assertEqual(result, expected_result)

    def test_process_queue_single_push_pop(self):
        # given
        commands = ["+ 10", "-"]
        expected_result = [10]

        # when
        result = process_queue([commands])

        # then
        self.assertEqual(result, expected_result)

    def test_process_queue_multiple_push_pop(self):
        # given
        commands = ["+ 5", "+ 10", "-", "+ 15", "-", "-", "+ 20", "-"]
        expected_result = [5, 10, 15, 20]

        # when
        result = process_queue([commands])

        # then
        self.assertEqual(result, expected_result)

    def test_process_queue_large_input(self):
        # given
        commands = ["+ " + str(i) for i in range(1, 100001)] + ["-"] * 100000
        expected_result = list(range(1, 100001))

        # when
        result = process_queue([commands])

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_used_memory_and_time(self):
        # given
        commands = ["+ 1", "+ 2", "-", "+ 3", "-", "-"]
        expected_result = [1, 2, 3]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = process_queue([commands])
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_queue([commands])
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Затрачено {time_end} секунд, превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Затрачено {memory} MB, превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
