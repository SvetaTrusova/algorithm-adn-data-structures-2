import os
import psutil
import time


def memory_usage_process():
    """Возвращает общее количество памяти (в байтах), использованное текущим процессом."""
    process = psutil.Process(os.getpid())  # Получаем объект текущего процесса
    return process.memory_info().rss / 2**20  # rss - Resident Set Size, фактическое использование памяти процессом


def read_input(path_input) -> tuple[int, list[int]]:
    """
    Функция для чтения входных данных из файла 'input.txt'.

    Возвращает список строк без символов перевода строки.
    """
    with open(path_input, "r") as file:
        n = int(file.readline())
        massive = [int(a) for a in file.readline().split()]
        return n, massive


def read_file_line(path: str, num: int) -> str:
    """
    Открывает файл -> считывает содержимое построчно в виде [[][]] -> num отвечает за номер строки (с 0!!!!)
    """
    line = open(path, "r").readlines()[num]
    return line


def write_output(string, path_output) -> None:
    """
    Функция для записи выходных данных в файл 'output.txt'.
    """
    with open(path_output, "w", encoding="utf-8") as file:
        file.write(string)


def normVid(array: list) -> str:
    s = ''
    for i in range(len(array) - 1):
        s += str(array[i]) + ' '
    s += str(array[-1])
    return s


def time_execution(funcs, *args, **kwargs):
    start_time = time.time()
    result = funcs(*args, **kwargs)
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time: .4f} секунд.")
    return result


def insertionsort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data


def insertionsort_not_increasing(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key > data[j]:
            data[j+1], data[j] = data[j], data[j+1]
            j -= 1
        data[j+1] = key
    return data


def insertion_sort(n, data):
    indexes = [1]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                i, j = j, i
        indexes.append(i+1)
    return data, indexes


def selectionsort(data):
    for i in range(len(data) - 1):
        minim = i
        for j in range(i+1, len(data)):
            if data[minim] > data[j]:
                minim = j
        data[minim], data[i] = data[i], data[minim]
    return data


def bubblesort(n, data):
    for i in range(n-1): #не делаем последнюю проходку, потому что останется последний элемент
        for j in range(n - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def read_input_7(path_input):
    with open(path_input, 'r') as f:
        n = int(f.readline())
        massive1 = [float(a) for a in f.readline().split()]
    return n, massive1


def write_output_7(path_output, massive, n):
    with open(path_output, 'w') as f:
        f.write(str(massive[0][1]))
        f.write(' ')
        f.write(str(massive[n // 2][1]))
        f.write(' ')
        f.write(str(massive[-1][1]))