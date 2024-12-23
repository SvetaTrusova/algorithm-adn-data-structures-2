from lab1.utils import memory_usage_process, read_input_7, write_output_7

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def to_sort(lst, n):
    massive = [(lst[i], i + 1) for i in range(n)]
    massive = sorted(massive)
    return massive


def main(path_input, path_output):
    n, massive1 = read_input_7(path_input)
    massive = to_sort(massive1, n)
    print("Входные данные:")
    print(n)
    print(*massive1)
    norm_sorted_data = to_sort(massive, n)
    print("Результат:")
    print(str(massive[0][1]) + ' ' + str(massive[n // 2][1]) + ' ' + str(massive[-1][1]))
    write_output_7(path_output, norm_sorted_data, n)


print(f"Memory used by the current process: {memory_usage_process()} Megabytes")

if __name__ == '__main__':
    main(path_input, path_output)

