import math
from lab6.utils import open_file, write_file, measuring, print_input_output, memory_usage_process
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def is_fibonacci_number(number):
    x = int(number)
    f1 = 5 * x ** 2 + 4
    f2 = 5 * x ** 2 - 4
    return math.isqrt(f1) ** 2 == f1 or math.isqrt(f2) ** 2 == f2


def fibonacci_check(arr):
    result = []
    for number in arr:
        result.append("Yes" if is_fibonacci_number(number) else "No")
    return result


def main(path_input, path_output):
    n, nums = open_file(path_input)
    inputs = str(n) + '\n' + ''.join(nums)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = '\n'.join(fibonacci_check(nums))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
