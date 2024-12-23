from lab1.task7.src.task7 import to_sort
import time
import unittest


class TestFunctionTime(unittest.TestCase):

    def test_should__check_functions(self):
        # given
        expected_result = [(1, 1), (5, 3), (6, 2), (7, 4), (8, 5), (9, 6)]
        data = [1, 6, 5, 7, 8, 9]
        n = 6
        expected_time = 2

        # when
        time_st = time.perf_counter()
        result = to_sort(data, n)
        time_end = time.perf_counter() - time_st

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
