from lab3.utils import write_file, memory_usage_process, print_input_output, open_file
from lab3.task1.src.task1_1 import randomized_quick_sort
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def sum_of_every_tenth_element(a, b):
    list_got = [el_a * el_b for el_a in a for el_b in b]
    randomized_quick_sort(list_got, 0, len(list_got) - 1)
    summa_ten = sum(list_got[i] for i in range(0, len(list_got), 10))
    return summa_ten


def main(path_input, path_output):
    n, m, list_a, list_b = open_file(path_input)
    inputs = f"{n} {m}\n{' '.join(map(str, list_a))}\n{' '.join(map(str, list_b))}"

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = sum_of_every_tenth_element(list_a, list_b)

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(str(result), path_output)

    print_input_output(inputs=inputs, result=str(result))
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
