# Задание №1 по варианту  : `Сортировка слиянием`
Студентка ИТМО, Трусова Светлана Викторовна 467766

## Вариант 22

## Задание 
1.	Используя псевдокод процедур Merge и Merge-sort из презентации к Лекции 2 (страницы 6–7), напишите программу сортировки слиянием на Python и проверьте сортировку, создав несколько рандомных массивов, подходящих под параметры:
-	Формат входного файла (input.txt). В первой строке входного файла содержится число n (1 ≤ n ≤ 2 · 104) — число элементов в массиве. Во второй строке находятся n различных целых чисел, по модулю не превосходящих 109
-	Формат выходного файла (output.txt). Одна строка выходного файла с отсортированным массивом. Между любыми двумя числами должен стоять ровно один пробел.
2.	Для проверки можно выбрать наихудший случай, когда сортируется массив размера 1000, 104, 105 чисел порядка 109, отсортированных в обратном порядке; наилучший, когда массив уже отсортирован, и средний. Сравните, например, с сортировкой вставкой на этих же данных.
3.	Перепишите процедуру Merge так, чтобы в ней не использовались сигнальные значения. Сигналом к остановке должен служить тот факт, что все элементы массива L или R скопированы обратно в массив A, после чего в этот массив копируются элементы, оставшиеся в непустом массиве, или перепишите процедуру Merge (и, соответственно, Merge-sort) так, чтобы в ней не использовались значения границ и середины - p, r и q.


## Input / Output 

| Input             | Output            |
|-------------------|-------------------|
| 6 5 4 3 2 1       | 1 2 3 4 5 6       |
| 31 41 59 26 41 58 | 26 31 41 41 58 59 |
| -1 3 -5 33 2      | -5 -1 2 3 33      |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SvetaTrusova/algorithms-and-data-structures-2.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures-2/lab2
   ```
3. Запустите программу:
   ```bash
   python task1/src/task1.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest -v lab2.task1.tests.test_2_1.py
```