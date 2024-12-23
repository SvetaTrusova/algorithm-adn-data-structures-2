import time
import tracemalloc
import psutil
import os


def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()

        try:
            if len(data[1:]) == int(data[0]):
                n = int(data[0])
                points = list()
                for i in range(1, n + 1):
                    line = data[i]
                    points.append(line)
                return n, points
        except ValueError:
            return data


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


def memory_usage_process():
    """Возвращает общее количество памяти (в байтах), использованное текущим процессом."""
    process = psutil.Process(os.getpid())  # Получаем объект текущего процесса
    return process.memory_info().rss / 2**20  # rss - Resident Set Size, фактическое использование памяти процессом
