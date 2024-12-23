from lab2.utils import open_file, write_file, measuring, print_input_output, memory_usage_process
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def merge_output(arr, temp_arr, left, mid, right, res):
    left_i = left
    right_i = mid + 1
    merged_i = left

    while left_i <= mid and right_i <= right:
        if arr[left_i] <= arr[right_i]:
            temp_arr[merged_i] = arr[left_i]
            left_i += 1
        else:
            temp_arr[merged_i] = arr[right_i]
            right_i += 1
        merged_i += 1

    while left_i <= mid:
        temp_arr[merged_i] = arr[left_i]
        left_i += 1
        merged_i += 1

    while right_i <= right:
        temp_arr[merged_i] = arr[right_i]
        right_i += 1
        merged_i += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    if (right - left + 1) > 1:
        res.append(f"{left + 1} {right + 1} {arr[left]} {arr[right]}")


def merge_sort_output(list_arr, temp, left_i, right_i, res):
    if left_i < right_i:
        middle = (left_i + right_i) // 2

        merge_sort_output(list_arr, temp, left_i, middle, res)
        merge_sort_output(list_arr, temp, middle + 1, right_i, res)
        merge_output(list_arr, temp, left_i, middle, right_i, res)


def main(input_file, output_file):
    n, arr = open_file(input_file)
    print("Входные данные:")
    print(n)
    print(*arr)

    res = list()
    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    merge_sort_output(arr, [0] * n, 0, n - 1, res)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    result = "\n".join(map(str, res)) + '\n' + " ".join(map(str, arr))

    print(f"Результат: \n{result}")
    write_file(result, output_file)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
