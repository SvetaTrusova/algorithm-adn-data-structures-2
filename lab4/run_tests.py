import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    suite = unittest.TestSuite()

    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)

    test_files = [
        'lab4.task1.tests.test_4_1',
        'lab4.task2.tests.test_4_2',
        'lab4.task4.tests.test_4_4',
        'lab4.task5.tests.test_4_5',
        'lab4.task6.tests.test_4_6',
        'lab4.task8.tests.test_4_8',
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
