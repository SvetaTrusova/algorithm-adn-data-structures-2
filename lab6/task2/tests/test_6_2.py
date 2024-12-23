import unittest
import tracemalloc
import time
from lab6.task2.src.task2 import manage_phonebook


class TestPhonebook(unittest.TestCase):

    def test_add_and_find(self):
        # Given
        data = [
            "add 1234567890 John",
            "add 9876543210 Alice",
            "find 1234567890",
            "find 9876543210"
        ]
        expected = ["John", "Alice"]

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_add_and_delete(self):
        # Given
        data = [
            "add 1234567890 John",
            "add 9876543210 Alice",
            "del 1234567890",
            "find 1234567890",
            "find 9876543210"
        ]
        expected = ["not found", "Alice"]

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_find_non_existing(self):
        # Given
        data = [
            "find 1234567890",
            "add 9876543210 Alice",
            "find 1234567890",
            "find 9876543210"
        ]
        expected = ['not found', 'not found', 'Alice']

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_delete_non_existing(self):
        # Given
        data = [
            "add 1234567890 John",
            "del 9876543210",  # номер не существует
            "find 1234567890"
        ]
        expected = ["John"]

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_empty_phonebook(self):
        # Given
        data = [
            "find 1234567890",  # телефонная книга пуста
            "add 1234567890 John",
            "find 1234567890"
        ]
        expected = ["not found", "John"]

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_operations(self):
        # Given
        data = [
            "add 1111111111 Tom",
            "add 2222222222 Jane",
            "add 3333333333 Bob",
            "del 2222222222",
            "find 2222222222",
            "find 1111111111",
            "find 3333333333"
        ]
        expected = ["not found", "Tom", "Bob"]

        # When
        result = manage_phonebook(data)

        # Then
        self.assertEqual(result, expected)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = ["not found", "Tom", "Bob"]
        data =[
            "add 1111111111 Tom",
            "add 2222222222 Jane",
            "add 3333333333 Bob",
            "del 2222222222",
            "find 2222222222",
            "find 1111111111",
            "find 3333333333"
        ]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = manage_phonebook(data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
