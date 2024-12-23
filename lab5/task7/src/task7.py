import time
from lab5.utils import memory_usage_process, read_input, write_output, normVid

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def max_heapify(arr, n, i):
    """Восстановление кучи (max-heapify) с использованием итерации"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    """Пирамидальная сортировка в убывающем порядке"""
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

    return arr


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print(f"Входные данные: \n{n}")
    print(*arr)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    sorted_arr = heap_sort(arr)
    norm_sorted_arr = str(normVid(sorted_arr))

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    print(f"Результат:\n{norm_sorted_arr}")
    write_output(norm_sorted_arr, path_output)

    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
