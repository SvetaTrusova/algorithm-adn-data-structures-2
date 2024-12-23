import time
import tracemalloc


def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()

        try:

            if len(data) == 2:
                money, k = map(int, data[0].split())
                coins = list(map(int, data[1].split()))
                return money, k, coins

        except ValueError:
            return str(data[0][:-1]), str(data[1])

        if len(data) == 4:
            n = int(data[0])
            a = list(map(int, data[1].split()))
            m = int(data[2])
            b = list(map(int, data[3].split()))
            return n, a, m, b

        elif len(data) == 6:
            n = int(data[0])
            a = list(map(int, data[1].split()))
            m = int(data[2])
            b = list(map(int, data[3].split()))
            l = int(data[4])
            c = list(map(int, data[5].split()))
            return n, a, m, b, l, c


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