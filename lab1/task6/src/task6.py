from lab1.utils import bubblesort, read_input, write_output, normVid, memory_usage_process

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def to_sort(n, data):
    sorted_data = bubblesort(n, data)
    norm_sorted_data = normVid(sorted_data)
    return norm_sorted_data


def main(path_input, path_output):
    n, data = read_input(path_input)
    print("Входные данные:")
    print(n)
    print(*data)
    norm_sorted_data = to_sort(n, data)
    print("Результат:")
    print(norm_sorted_data)
    write_output(norm_sorted_data, path_output)


print(f"Memory used by the current process: {memory_usage_process()} Megabytes")


if __name__ == '__main__':
    main(path_input, path_output)
