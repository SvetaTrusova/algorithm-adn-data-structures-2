import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    suite = unittest.TestSuite()

    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)

    test_files = [
        'lab3.task1.tests.test_3_1',
        'lab3.task2.tests.test_3_2',
        'lab3.task3.tests.test_3_3',
        'lab3.task4.tests.test_3_4',
        'lab3.task5.tests.test_3_5',
        'lab3.task6.tests.test_3_6',
    ]

    for test_file in test_files:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        except ModuleNotFoundError as e:
            print(f"Ошибка при добавлении теста {test_file}: {e}")

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()
