from lab4.utils import open_file, write_file, print_input_output, memory_usage_process
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def queue_min(commands):
    queue = list()
    result = list()
    for command in commands:
        if command[0] == "+":
            queue.append(int(command.split()[1]))
        elif command[0] == "-":
            queue.pop(0)
        elif command[0] == '?':
            result.append(min(queue))
    return result


def main(path_input, path_output):
    m, commands = open_file(path_input)
    inputs = (str(m) + "\n" + "\n".join(commands))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = '\n'.join(map(str, queue_min(commands)))

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    # Записываем результат в выходной файл
    write_file(result, path_output)

    # Выводим информацию о результатах
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)