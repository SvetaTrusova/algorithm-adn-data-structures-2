# Задание №5 по выбору : `Сортировка выбором`
Студентка ИТМО,  Трусова Светлана Викторовна 467766

## Вариант 22

## Задание 5
Рассмотрим сортировку элементов массива , которая выполняется следующим
образом. Сначала определяется наименьший элемент массива , который ставится
на место элемента A[1]. Затем производится поиск второго наименьшего элемента
массива A, который ставится на место элемента A[2]. Этот процесс продолжается
для первых n − 1 элементов массива A.
Напишите код этого алгоритма, также известного как сортировка выбором
(selection sort). Определите время сортировки выбором в наихудшем случае и в
среднем случае и сравните его со временем сортировки вставкой.
Формат входного и выходного файла и ограничения - как в задаче 1.

## Input / Output 

| Input                | Output               |
|----------------------|----------------------|
| 5                    | 2 2 45 75 456        |
| 2 45 75 2 456        |                      |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
      git clone https://github.com/SvetaTrusova/algorithm-and-data-structures-2.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures-2\lab1\task5
   ```
3. Запустите программу:
   ```bash
   python src/task5.py
   ```

4. Запуск тестов:
   ```bash
   python -m unittest discover -s tests -p "task5.py"
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest discover -s tests -p "task5.py"
```