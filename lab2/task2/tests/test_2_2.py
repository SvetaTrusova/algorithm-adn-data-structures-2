from lab2.task2.src.task2 import merge_sort_output
import unittest
import datetime


class TestMergeSortOutput(unittest.TestCase):
    def test_should_sort_given_list(self):
        # Given
        unsorted_list = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_time = datetime.timedelta(2)
        expected_result = "\n".join(['1 2 1 8', '1 3 1 8', '4 5 1 4', '1 5 1 8', '6 7 3 7', '6 8 2 7',
                            '9 10 3 6', '6 10 2 7', '1 10 1 8', '1 1 2 2 3 3 4 6 7 8'])

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        res = list()
        merge_sort_output(unsorted_list, [0] * len(unsorted_list), 0, len(unsorted_list) - 1, res)
        result = "\n".join(map(str, res)) + '\n' + " ".join(map(str, unsorted_list))
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()