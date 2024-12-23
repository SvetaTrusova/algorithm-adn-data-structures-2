from lab2.task3.src.task3 import to_sort, count_inversions
import time
import tracemalloc
import unittest


class TestInversions(unittest.TestCase):
    def test_should_check_single_element(self):
        """Тест на массив с одним элементом"""
        # given
        arr = [1]

        # then
        self.assertEqual(count_inversions(arr), 0)

    def test_should_check_sorted_array(self):
        """Тест на отсортированный массив (0 инверсий)"""
        # given
        arr = [1, 2, 3, 4, 5]

        # then
        self.assertEqual(count_inversions(arr), 0)

    def test_should_check_reverse_sorted_array(self):
        """Тест на массив, отсортированный в обратном порядке (макс. инверсий)"""
        # given
        arr = [5, 4, 3, 2, 1]

        # then
        self.assertEqual(count_inversions(arr), 10)

    def test_should_check_array_with_few_inversions(self):
        """Тест на массив с несколькими инверсиями"""
        # given
        arr = [1, 3, 2, 4, 5]

        # then
        self.assertEqual(count_inversions(arr), 1)

    def test_should_check_array_with_more_inversions(self):
        """Тест на массив с несколькими инверсиями"""
        # given
        arr = [3, 1, 2, 5, 4]

        # then
        self.assertEqual(count_inversions(arr), 3)

    def test_should_check_large_array(self):
        """Тест на большой массив"""
        # given
        arr = list(range(100000, 0, -1))  # Массив от 100000 до 1

        # then
        self.assertEqual(count_inversions(arr), 4999950000)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = 2
        data = [1, 24, 5, 34, 1000, 374]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = to_sort(data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()

