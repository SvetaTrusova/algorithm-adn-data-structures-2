from lab6.utils import write_file, open_file, print_input_output, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def fibonacci_check(n, data):
    result = []
    s = set()

    for i in range(n):
        line = data[i].split()
        operation = line[0]
        x = int(line[1])

        if operation == 'A':
            s.add(x)
        elif operation == 'D':
            s.discard(x)
        elif operation == '?':
            if x in s:
                result.append('Y')
            else:
                result.append('N')

    return result


def main(path_input, path_output):
    n, commands = open_file(path_input)
    inputs = (str(n) + "\n" + "".join(commands))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = '\n'.join(fibonacci_check(n, commands))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)