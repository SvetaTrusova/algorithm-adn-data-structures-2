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
        data = file.read().strip().replace(",", " ").split()
        citations = list(map(int, data))
        return citations


def read_file_line(path: str, num: int) -> str:
    """
    Открывает файл -> считывает содержимое построчно в виде [[][]] -> num отвечает за номер строки (с 0!!!!)
    """
    line = open(path, "r").readlines()[num]
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
            return int(data[0])

        elif len(data) == 2:
            if ord(data[1][0]) in range(65, 91):
                arr = [i for i in data[1]]
            else:
                arr = list(map(int, data[1].split()))

            n = data[0]
            if len(n.split()) == 1:
                n = int(n)
                return n, arr
            else:
                n, k =map(int, n.split())
                return n, k, arr

        elif len(data) == 3:
            n, m = map(int, data[0].split())
            a = list(map(int, data[1].split()))
            b = list(map(int, data[2].split()))
            return n, m, a, b

        elif len(data[1:]) == list(map(int, data[0].split()))[0]:
            n = int(data[0])
            points = list()
            for i in range(1, n):
                line = list(map(int, data[i].split()))
                points.append(line)
            return n, points

        else:
            n, k = map(int, data[0].split())
            intervals = [list(map(int, i.split())) for i in data[1:n + 1]]
            dots = list(map(int, data[n + 1].split()))
            return n, k, intervals, dots



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