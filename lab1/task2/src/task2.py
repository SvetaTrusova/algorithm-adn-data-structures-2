from lab1.utils import insertion_sort, read_input, write_output, memory_usage_process, normVid
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def to_sort(n, data):
    sorted_data, sorted_indexes = insertion_sort(n, data)
    str_norm_sorted_data = normVid(sorted_data)  # Преобразуем элементы списка в строку, разделяя пробелами
    str_norm_sorted_indexes = normVid(sorted_indexes)  # То же для второго массива
    output_string = str_norm_sorted_indexes + '\n' + str_norm_sorted_data + '\n'
    return output_string


def main(path_input, path_output):
    n, data = read_input(path_input)
    print("Входные данные:")
    print(n)
    print(*data)
    print("Результат:")
    norm_sorted_data = to_sort(n, data)
    print(norm_sorted_data)
    write_output(norm_sorted_data, path_output)
    if 1 <= n <= 10 ** 3:
        write_output(norm_sorted_data, path_output)
    else:
        print('Введенные данные не соответствуют условию')


print(f"Memory used by the current process: {memory_usage_process()} Megabytes")


if __name__ == '__main__':
    main(path_input, path_output)
