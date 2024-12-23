import random
from lab3.utils import open_file, write_file, memory_usage_process, print_input_output
import time


path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def to_sort(n, arr):
    result = randomized_quick_sort(arr, 0, n - 1)
    return result


def partition_upd(arr, left_index, right_index):
    x = arr[left_index]
    m_left = left_index
    m_right = right_index
    i = left_index

    while i <= m_right:
        if arr[i] < x:
            arr[m_left], arr[i] = arr[i], arr[m_left]
            m_left += 1
            i += 1
        elif arr[i] > x:
            arr[i], arr[m_right] = arr[m_right], arr[i]
            m_right -= 1
        else:
            i += 1

    return m_left, m_right


def randomized_quick_sort(arr, left_index, right_index):
    if left_index < right_index:
        random_num = random.randint(left_index, right_index)
        arr[left_index], arr[random_num] = arr[random_num], arr[left_index]
        m1, m2 = partition_upd(arr, left_index, right_index)
        randomized_quick_sort(arr, left_index, m1 - 1)
        randomized_quick_sort(arr, m2 + 1, right_index)
    return arr


def main(path_input, path_output):
    n, arr = open_file(path_input)
    inputs = str(n) + '\n' + ' '.join(map(str, arr))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = ' '.join(map(str, randomized_quick_sort(arr, 0, n - 1)))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
