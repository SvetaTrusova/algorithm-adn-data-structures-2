from lab4.utils import open_file, write_file, memory_usage_process, print_input_output, read_file_line
import time
from collections import deque

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def process_queue(commands):
    queue = deque()
    result = []

    for command in commands[0]:
        parts = command.split()
        if parts[0] == '+':
            queue.append(int(parts[1]))
        elif parts[0] == '-':
            result.append(queue.popleft())

    return result


def main(path_input, path_output):
    m = read_file_line(path_input)
    commands = open_file(path_input)[1:]

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = process_queue(commands)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file("\n".join(map(str, result)), path_output)

    print_input_output(inputs=list(map(lambda x: x.strip(), m)), result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
