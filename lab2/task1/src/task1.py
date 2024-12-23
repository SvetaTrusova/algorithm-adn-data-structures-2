from lab2.utils import read_input, write_output, normVid, memory_usage_process
import time


path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def merge(left, right):
    """Слияние двух отсортированных массивов left и right"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    """Реализация сортировки слиянием"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def to_sort(arr):
    sorted_arr = merge_sort(arr)
    norm_sorted_arr = normVid(sorted_arr)
    return norm_sorted_arr


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print("Входные данные:")
    print(n)
    print(*arr)
    memory_before = memory_usage_process()
    norm_sorted_arr = to_sort(arr)
    memory_after = memory_usage_process()
    time_st = time.perf_counter()
    result = to_sort(arr)
    time_end = time.perf_counter() - time_st
    print(f"Результат: \n{norm_sorted_arr}")
    write_output(norm_sorted_arr, path_output)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
