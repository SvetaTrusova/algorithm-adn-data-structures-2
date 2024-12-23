import os
import psutil
import time
import tracemalloc


def memory_usage_process():
    """Возвращает общее количество памяти (в байтах), использованное текущим процессом."""
    process = psutil.Process(os.getpid())  # Получаем объект текущего процесса
    return process.memory_info().rss / 2**20  # rss - Resident Set Size, фактическое использование памяти процессом


def read_input(path_input):
    """
    Функция для чтения входных данных из файла 'input.txt'.

    Возвращает список строк без символов перевода строки.
    """
    with open(path_input, "r") as file:
        n = int(file.readline())
        massive = [str(a) for a in file.readline().split()]
        return n, massive


def read_file_line(path: str) -> str:
    """
    Открывает файл -> считывает содержимое построчно в виде [[][]] -> num отвечает за номер строки (с 0!!!!)
    """
    line = open(path, "r").readlines()
    return line


def write_output(arr, path_output) -> None:
    """
    Функция для записи выходных данных в файл 'output.txt'.
    """
    with open(path_output, "w", encoding="utf-8") as file:
        file.write(" ".join(map(str, arr)) + "\n")


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
        if len(data) == 1:
            return data[0]
        elif len(data) == 2:
            return int(data[0]), data[1]
        elif len(data[1:]) == int(data[0]):
            n = int(data[0].rstrip())
            list_input = list(data[i].rstrip() for i in range(1, n + 1))
            return n, list_input
        else:
            return list(map(int, data))


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