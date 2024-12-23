from lab2.utils import read_input, write_output, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def is_heap(n, arr):
    """Проверка, является ли массив кучей"""
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1

        if left <= n and arr[i - 1] > arr[left - 1]:
            return "NO"

        if right <= n and arr[i - 1] > arr[right - 1]:
            return "NO"

    return "YES"


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print(f"Входные данные: \n{n}")
    print(*arr)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = is_heap(n, arr)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    print(f"Результат:\n{result}")
    write_output(result, path_output)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
