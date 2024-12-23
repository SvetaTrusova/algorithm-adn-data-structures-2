import unittest
import time
import tracemalloc
from lab3.task2.src.task2 import anti_quick_sort


# Тестовая оболочка
class TestAntiQuickSort(unittest.TestCase):

    def test_anti_quick_sort(self):
        # given
        n = 5
        expected_result = [5, 4, 3, 2, 1]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_anti_quick_sort_single_element(self):
        # given
        n = 1
        expected_result = [1]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_anti_quick_sort_large(self):
        # given
        n = 100
        expected_result = list(range(100, 0, -1))

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_large_input(self):
        # given
        n = 100000

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result[0], n)
        self.assertEqual(result[-1], 1)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = [3, 2, 1]
        expected_time = 2
        expected_memory = 256
        n = 3

        # when
        time_st = time.perf_counter()
        result = anti_quick_sort(n)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = anti_quick_sort(n)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
