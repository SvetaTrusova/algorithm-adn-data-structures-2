from lab3.utils import write_file, memory_usage_process, print_input_output, read_input
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def h_index(citations):
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i

    return len(citations)


def main(path_input, path_output):
    citations = read_input(path_input)
    inputs = ', '.join(map(str, citations))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = h_index(citations)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(str(result), path_output)

    print_input_output(inputs=inputs, result=str(result))
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
