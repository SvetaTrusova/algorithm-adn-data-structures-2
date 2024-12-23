from lab2.utils import memory_usage_process, open_file, write_file,  print_input_output
import time


path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def binary_search(list_arr, number):
    left, right = 0, len(list_arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_arr[middle] == number:
            return middle
        elif list_arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def search_elements(array, targets):
    result = []
    for target in targets:
        index = binary_search(array, target)
        result.append(index)
    return result


def main(path_input, path_output):
    n, arr, k, search_arr = open_file(path_input)
    print("Входные данные:")
    print(n)
    print(*arr)
    print(k)
    print(*search_arr)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = ' '.join(map(str, search_elements(arr, search_arr)))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    print(f"Результат: \n {result}")

    write_file(result, path_output)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
