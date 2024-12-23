import unittest
from lab7.task3.src.task3 import edit_distance


class TestEditDistance(unittest.TestCase):

    def test_no_operations(self):
        # Строки одинаковые, редакционное расстояние должно быть 0
        a = "abc"
        b = "abc"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 0)
        self.assertEqual(operations, [])

    def test_single_change(self):
        # Строки отличаются только одним символом, редакционное расстояние должно быть 1
        a = "abc"
        b = "abd"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 1)
        self.assertEqual(operations, ["change c d"])

    def test_insertion(self):
        # Вставка одного символа, редакционное расстояние должно быть 1
        a = "abc"
        b = "abdc"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 1)
        self.assertEqual(operations, ["add d"])

    def test_deletion(self):
        # Удаление одного символа, редакционное расстояние должно быть 1
        a = "abc"
        b = "ab"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 1)
        self.assertEqual(operations, ["del c"])

    def test_multiple_operations(self):
        # Сложный случай с несколькими операциями
        a = "kitten"
        b = "sitting"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 3)
        self.assertTrue("change k s" in operations)
        self.assertTrue("change e i" in operations)
        self.assertTrue("add g" in operations)

    def test_empty_string(self):
        # Преобразование пустой строки в не пустую, редакционное расстояние равно длине строки
        a = ""
        b = "abc"
        dist, operations = edit_distance(a, b)
        self.assertEqual(dist, 3)
        self.assertEqual(operations, ["add a", "add b", "add c"])

    def test_large_case(self):
        # Тест с более длинными строками
        a = "abcdef" * 500
        b = "abcfgh" * 500
        dist, operations = edit_distance(a, b)
        self.assertTrue(dist > 0)  # Убедимся, что редакционное расстояние не равно 0


if __name__ == '__main__':
    unittest.main()
