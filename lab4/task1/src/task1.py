from lab4.utils import open_file, write_file, memory_usage_process, print_input_output
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def stack_commands(commands):
    stack = list()
    deleted_el = list()
    for command in commands:
        if command[0] == '+':
            stack.append(int(command.split('+')[1]))
        elif command == '-' and len(stack) != 0:
            element = stack.pop()
            deleted_el.append(element)
    return deleted_el


def main(input_file, output_file):
    m, commands = open_file(input_file)
    inputs = (str(m) + "\n" + "\n".join(commands))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = '\n'.join(map(str, stack_commands(commands)))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)