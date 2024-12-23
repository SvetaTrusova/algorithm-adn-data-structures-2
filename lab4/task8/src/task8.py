from lab4.utils import open_file, write_file, memory_usage_process, print_input_output
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def postfix_calculate(expression):
    stack = []
    actions = ['+', '-', '*', '/']
    for symbol in expression.split():
        if symbol not in actions:
            stack.append(int(symbol))
        else:
            b = stack.pop()
            a = stack.pop()
            if symbol == '+':
                stack.append(a + b)
            elif symbol == '-':
                stack.append(a - b)
            elif symbol == '*':
                stack.append(a * b)
            elif symbol == '/':
                stack.append(int(a / b))
    return stack[0]


def main(path_input, path_output):
    m, commands = open_file(path_input)
    inputs = (str(m) + "\n" + "".join(commands))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = str(postfix_calculate(commands))

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