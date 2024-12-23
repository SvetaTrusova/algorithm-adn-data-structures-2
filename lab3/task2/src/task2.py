from lab3.utils import open_file, write_file, memory_usage_process, print_input_output
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def anti_quick_sort(n):
    return list(range(n, 0, -1))


def main(path_input, path_output):
    n = open_file(path_input)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = ' '.join(map(str, anti_quick_sort(n)))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)

    print_input_output(inputs=str(n), result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)

