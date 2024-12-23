from lab2.utils import read_input, write_output, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def min_heapify(arr, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))
        min_heapify(arr, n, smallest, swaps)


def build_min_heap(arr):
    n = len(arr)
    swaps = []

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i, swaps)

    return swaps


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print(f"Входные данные: \n{n}")
    print(*arr)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    swaps = build_min_heap(arr)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_output(f"{len(swaps)}\n" + "\n".join([f"{i} {j}" for i, j in swaps]), path_output)
    print(f"Результат:\n{swaps}")
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
