import unittest
import time
import tracemalloc
from lab6.task5.src.task5 import process_elections


class TestProcessElections(unittest.TestCase):

    def test_single_candidate(self):
        # Given
        candidates_input = [
            "Alice 100"
        ]
        expected = ["Alice 100"]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_candidates(self):
        # Given
        candidates_input = [
            "Alice 100",
            "Bob 50",
            "Charlie 75"
        ]
        expected = [
            "Alice 100",
            "Bob 50",
            "Charlie 75"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_same_candidate_multiple_votes(self):
        # Given
        candidates_input = [
            "Alice 100",
            "Bob 50",
            "Alice 50"
        ]
        expected = [
            "Alice 150",
            "Bob 50"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_empty_input(self):
        # Given
        candidates_input = []
        expected = []

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_large_number_of_votes(self):
        # Given
        candidates_input = [
            "Alice 1000000000",
            "Bob 500000000",
            "Charlie 750000000"
        ]
        expected = [
            "Alice 1000000000",
            "Bob 500000000",
            "Charlie 750000000"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_sorted_candidates(self):
        # Given
        candidates_input = [
            "Charlie 75",
            "Alice 100",
            "Bob 50"
        ]
        expected = [
            "Alice 100",
            "Bob 50",
            "Charlie 75"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_multiple_votes_same_candidate(self):
        # Given
        candidates_input = [
            "Alice 100",
            "Alice 150",
            "Alice 200"
        ]
        expected = ["Alice 450"]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_candidate_with_zero_votes(self):
        # Given
        candidates_input = [
            "Alice 100",
            "Bob 0",
            "Charlie 50"
        ]
        expected = [
            "Alice 100",
            "Bob 0",
            "Charlie 50"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_alphabetical_order(self):
        # Given
        candidates_input = [
            "Bob 200",
            "Alice 150",
            "Charlie 300"
        ]
        expected = [
            "Alice 150",
            "Bob 200",
            "Charlie 300"
        ]

        # When
        result = process_elections(candidates_input)

        # Then
        self.assertEqual(result, expected)

    def test_should_check_used_memory_and_time(self):
        # given
        expected = ['Alice 150', 'Bob 200', 'Charlie 300']
        candidates_input = [
            "Bob 200",
            "Alice 150",
            "Charlie 300"
        ]
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = process_elections(candidates_input)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()

