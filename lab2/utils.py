import os
import psutil
import time
import tracemalloc

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

def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        if len(data) == 2:
            n = int(data[0])
            if ord(data[1][0]) in range(65, 91):
                arr = [i for i in data[1]]
            else:
                arr = list(map(int, data[1].split()))
            return n, arr
        if len(data) == 4:
            n1 = int(data[0])
            n2 = int(data[2])
            arr1 = list(map(int, data[1].split()))
            arr2 = list(map(int, data[3].split()))
            return n1, arr1, n2, arr2
        else:
            n = int(data[0].strip())
            arr1 = list()
            for i in range(1, n + 1):
                row = list(map(int, data[i].strip().split()))
                arr1.append(row)
            arr2 = list()
            for i in range(n + 1, 2 * n + 1):
                row = list(map(int, data[i].strip().split()))
                arr2.append(row)
        return arr1, arr2

def write_file(arr, file_name):
    with open(file_name, 'w') as file:
        if arr == str(arr):
            file.write(arr)
        else:
            if isinstance(arr, list):
                if isinstance(arr[0], list):
                    for r in arr:
                        file.write(' '.join(map(str, r)) + '\n')
                else:
                    file.write(' '.join(map(str, arr)))
            elif isinstance(arr, tuple):
                file.write(f"{' '.join(map(str, arr[0]))}\n")
                file.write(' '.join(map(str, arr[1])))
            else:
                file.write(arr)


def measuring(task_func, *args):
    start_time = time.perf_counter()
    tracemalloc.start()

    task_func(*args)
    print(f'Время работы: {time.perf_counter() - start_time}\n'
          f'Память: {str(tracemalloc.get_traced_memory()[1] / 1024 ** 2)} Мб')
    tracemalloc.stop()


def print_input_output(inputs=str, result=str):
    print(f'Входные данные: \n{inputs}')
    print(f'Результат: \n{result}')