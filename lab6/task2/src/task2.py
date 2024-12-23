from lab6.utils import open_file, write_file, measuring, print_input_output, memory_usage_process
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def manage_phonebook(data):
    phonebook = {}
    result = []

    for query in data:
        command = query.split()[0]

        if command == 'add':
            phonebook[query.split()[1]] = query.split()[2]

        elif command == 'del':
            number = query.split()[1]
            if number in phonebook:
                del phonebook[number]

        elif command == 'find':
            number = query.split()[1]
            if number in phonebook:
                result.append(phonebook[number])
            else:
                result.append('not found')

    return result


def main(path_input, path_output):
    n, commands = open_file(path_input)
    inputs = (str(n) + "\n" + "".join(commands))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = '\n'.join(manage_phonebook(commands))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)