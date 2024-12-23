from lab2.utils import read_input, write_output, normVid, memory_usage_process
import time


path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    count = arr.count(candidate)

    if count > len(arr) // 2:
        return 1  # Элемент существует
    else:
        return 0  # Элемента нет


def to_sort(arr):
    element = majority_element(arr)
    return element


def main(path_input, path_output):
    n, arr = read_input(path_input)

    print("Входные данные:")
    print(n)
    print(*arr)

    memory_before = memory_usage_process()
    result = to_sort(arr)
    memory_after = memory_usage_process()
    time_st = time.perf_counter()
    result = to_sort(arr)
    time_end = time.perf_counter() - time_st

    print(f"Результат: \n {result}")

    write_output(str(result), path_output)

    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
