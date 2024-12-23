from lab1.utils import insertion_sort
from lab1.task2.src.task2 import to_sort
import time
import unittest


class TestInsertionSort1(unittest.TestCase):
    def test_should_shouldsingle_element(self):
        """Тест на список с одним элементом"""
        # given
        data = [42]
        exeptepted_data = [42]
        exeptepted_indexes = [1]

        # when
        sorted_data, indexes = insertion_sort(len(data), data)

        # then
        self.assertEqual(sorted_data, exeptepted_data)  # Список не изменится
        self.assertEqual(indexes, exeptepted_indexes)  # Индекс остался на месте

    def test_should_sorted_list(self):
        """Тест на уже отсортированный список"""
        # given
        exeptepted_data = [1, 2, 3, 4, 5]
        exeptepted_indexes = [1, 2, 3, 4, 5]
        data = [1, 2, 3, 4, 5]

        # when
        sorted_data, indexes = insertion_sort(len(data), data)

        # then
        self.assertEqual(sorted_data, exeptepted_data)  # Список уже отсортирован
        self.assertEqual(indexes, exeptepted_indexes)  # Индексы должны быть на своих местах

    def test_should_reverse_order(self):
        """Тест на список в обратном порядке"""
        # given
        exeptepted_data = [1, 2, 3, 4, 5]
        exeptepted_indexes = [1, 1, 1, 1, 1]
        data = [5, 4, 3, 2, 1]

        # when
        sorted_data, indexes = insertion_sort(len(data), data)

        # then
        self.assertEqual(sorted_data, exeptepted_data)  # Ожидаемый отсортированный список
        self.assertEqual(indexes, exeptepted_indexes)  # Индексы будут следовать за сортировкой


class TestTimeMemory(unittest.TestCase):

    def test_should_check_functions(self):
        # given
        expected_result = '1 2 2 4 5 5\n1 5 24 34 374 1000\n'
        data = [1, 24, 5, 34, 1000, 374]
        n = 6
        expected_time = 2

        # when
        time_st = time.perf_counter()
        result = to_sort(n, data)
        time_end = time.perf_counter() - time_st

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()
