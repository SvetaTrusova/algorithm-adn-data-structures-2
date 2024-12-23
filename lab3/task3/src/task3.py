from lab3.utils import open_file, write_file, memory_usage_process, print_input_output
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def pugalo_sort(n, k, arr):
    groups = [[] for _ in range(k)]

    for i in range(n):
        groups[i % k].append(arr[i])

    for group in groups:
        group.sort()

    sorted_arr = []
    for i in range(n):
        sorted_arr.append(groups[i % k].pop(0))

    if sorted_arr == sorted(arr):
        return "ДА"
    else:
        return "НЕТ"


def main(path_input, path_output):
    n, k, arr = open_file(path_input)
    inputs = str(n) + ' ' + str(k) + '\n' + ' '.join(map(str, arr))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = pugalo_sort(n, k, arr)

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)

