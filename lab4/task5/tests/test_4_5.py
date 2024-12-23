import unittest
from lab4.task5.src.task5 import process_stack
import time
import tracemalloc

class StackMaxTestCase(unittest.TestCase):
    def test_should_return_correct_results_for_simple_max_operations(self):
        # given
        commands = ["push 2", "push 1", "max", "pop", "max"]
        expected_result = [2, 2]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_results_for_push_pop_and_max(self):
        # given
        commands = ["push 1", "push 2", "max", "pop", "max"]
        expected_result = [2, 1]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_empty_result_for_no_max_operations(self):
        # given
        commands = ["push 1", "push 7", "pop"]
        expected_result = []

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_results_for_multiple_max_operations(self):
        # given
        commands = [
            "push 2",
            "push 3",
            "push 9",
            "push 7",
            "push 2",
            "max",
            "max",
            "max",
            "pop",
            "max",
        ]
        expected_result = [9, 9, 9, 9]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_results_for_repeated_max_operations(self):
        # given
        commands = ["push 7", "push 1", "push 7", "max", "pop", "max"]
        expected_result = [7, 7]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_used_memory_and_time(self):
        # given
        commands = ["push 2", "push 1", "max", "pop", "max"]
        expected_result = [2, 2]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = process_stack(commands)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = process_stack(commands)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024  # Конвертируем в МБ
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time,
                             f"Затрачено {time_end} секунд, превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Затрачено {memory} MB, превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
