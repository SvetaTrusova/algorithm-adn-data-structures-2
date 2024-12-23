from lab2.task5.src.task5 import to_sort, majority_element
import time
import tracemalloc
import unittest


class TestMajorityElement(unittest.TestCase):

    def test_should_check_simple_case(self):
        """Тест для простого случая с элементом большинства."""
        # given
        arr = [2, 3, 9, 2, 2]
        expected = 1

        # then
        self.assertEqual(majority_element(arr), expected)

    def test_should_check_no_majority_element(self):
        """Тест для массива без элемента большинства."""
        # given
        arr = [1, 2, 3, 4, 5]
        expected = 0

        # then
        self.assertEqual(majority_element(arr), expected)

    def test_should_check_single_element(self):
        """Тест для массива с одним элементом."""
        # given
        arr = [7]
        expected = 1

        # then
        self.assertEqual(majority_element(arr), expected)

    def test_should_check_all_same(self):
        """Тест для массива, где все элементы одинаковы."""
        # given
        arr = [8] * 100
        expected = 1

        # then
        self.assertEqual(majority_element(arr), expected)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = 0
        data = [1, 24, 5, 34, 1000, 374]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = to_sort(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = to_sort(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()