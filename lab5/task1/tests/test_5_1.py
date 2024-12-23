import unittest
import tracemalloc
import time
from lab5.task1.src.task1 import is_heap


class TestIsHeap(unittest.TestCase):

    def test_is_heap_with_valid_heap(self):
        """Тестируем случай, когда массив является кучей"""
        self.assertEqual(is_heap(5, [1, 2, 3, 4, 5]), "YES")
        self.assertEqual(is_heap(7, [1, 2, 3, 4, 5, 6, 7]), "YES")
        self.assertEqual(is_heap(3, [1, 3, 2]), "YES")
        self.assertEqual(is_heap(6, [1, 2, 3, 4, 5, 6]), "YES")

    def test_is_heap_with_invalid_heap(self):
        """Тестируем случай, когда массив не является кучей"""
        self.assertEqual(is_heap(5, [5, 2, 3, 4, 1]), "NO")
        self.assertEqual(is_heap(7, [7, 2, 6, 4, 5, 3, 1]), "NO")
        self.assertEqual(is_heap(3, [3, 1, 2]), "NO")
        self.assertEqual(is_heap(6, [6, 5, 3, 4, 2, 1]), "NO")

    def test_is_heap_with_edge_case(self):
        """Тестируем крайние случаи"""
        self.assertEqual(is_heap(1, [1]), "YES")  # Массив с одним элементом всегда куча
        self.assertEqual(is_heap(2, [2, 1]), "NO")  # Массив с двумя элементами
        self.assertEqual(is_heap(2, [1, 2]), "YES")  # Массив с двумя элементами
        self.assertEqual(is_heap(1, [2]), "YES")  # Еще один случай для одного элемента

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = 'YES'
        data = [1, 24, 5, 34, 1000, 374]
        n = 6
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = is_heap(n, data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
