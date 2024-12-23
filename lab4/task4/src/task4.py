from lab4.utils import open_file, write_file, memory_usage_process, print_input_output
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def check_brackets(data):
    stack = []
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for i, symb in enumerate(data, start=1):
        if symb in "([{":
            stack.append((symb, i))
        elif symb in ")]}":
            if not stack or stack[-1][0] != bracket_pairs[symb]:
                return i
            stack.pop()

    if stack:
        return stack[0][1]

    return "Success"


def main(path_input, path_output):
    s = open_file(path_input)
    inputs = (str(s))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = str(check_brackets(s))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)

    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
