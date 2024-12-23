import unittest
import datetime

from lab7.task1.src.task1 import coins_function


class TestCoinsFunction(unittest.TestCase):
    def test_should_make_coins_function(self):
        # Given
        money = 2
        coins = [1, 3, 4]
        expected_time = datetime.timedelta(1)
        expected_result = 2

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = coins_function(money, coins)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_make_coins_function(self):
        # Given
        money = 34
        coins = [1, 3, 4]
        expected_time = datetime.timedelta(1)
        expected_result = 9

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = coins_function(money, coins)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()