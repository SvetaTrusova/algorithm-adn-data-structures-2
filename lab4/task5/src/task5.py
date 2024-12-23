from lab4.utils import write_file, memory_usage_process, print_input_output, open_file
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            if popped_value == self.max_stack[-1]:
                self.max_stack.pop()

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None


def process_stack(operations):
    stack = MaxStack()
    results = []

    for operation in operations:
        if operation.startswith("push "):
            _, value = operation.split()
            stack.push(int(value))
        elif operation == "pop":
            stack.pop()
        elif operation == "max":
            results.append(stack.max())

    return results


def main(path_input, path_output):
    threads, tasks = open_file(path_input)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = process_stack(tasks)

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    # Записываем результат в выходной файл
    write_file(result, path_output)

    # Выводим информацию о результатах
    print_input_output(inputs=tasks, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
