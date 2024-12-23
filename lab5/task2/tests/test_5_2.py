import unittest
import tracemalloc
import time
from lab5.task2.src.task2 import calculate_tree_height


class TestCalculateTreeHeight(unittest.TestCase):

    def test_single_node(self):
        # given
        n = 1
        parents = [-1]
        expected_result = 1

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_simple_tree(self):
        # given
        n = 3
        parents = [-1, 0, 0]
        expected_result = 2

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_complex_tree(self):
        # given
        n = 5
        parents = [4, -1, 4, 1, 1]
        expected_result = 3

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_deep_tree(self):
        # given
        n = 5
        parents = [-1, 0, 1, 2, 3]
        expected_result = 5

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_tree_with_multiple_levels(self):
        # given
        n = 6
        parents = [-1, 0, 0, 1, 2, 2]
        expected_result = 3

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_tree_with_no_children(self):
        # given
        n = 4
        parents = [-1, -1, -1, -1]
        expected_result = 1

        # then
        self.assertEqual(calculate_tree_height(n, parents), expected_result)

    def test_should_check_used_memory_and_time(self):
        # given
        expected_result = 4
        data = [-1, 0, 4, 0, 3]
        n = 5
        expected_time = 2
        expected_memory = 256

        # when
        tracemalloc.start()
        time_st = time.perf_counter()
        result = calculate_tree_height(n, data)
        time_end = time.perf_counter() - time_st
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == '__main__':
    unittest.main()
