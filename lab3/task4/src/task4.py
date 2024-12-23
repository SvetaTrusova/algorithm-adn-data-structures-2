from lab3.utils import open_file, write_file, memory_usage_process, print_input_output
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def count_intervals(p, intervals, dots):
    nums = [0] * p
    for i in range(p):
        for interval in intervals:
            if interval[0] < dots[i] < interval[-1]:
                nums[i] += 1
    return nums


def main(path_input, path_output):
    s, p, intervals, dots = open_file(path_input)
    inputs = (str(s) + ' ' + str(p) + '\n' + "\n".join(" ".join(map(str, interval)) for interval in intervals) +
              '\n' + " ".join(map(str, dots)))

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    result = count_intervals(p, intervals, dots)

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)

    print_input_output(inputs=inputs, result=" ".join(map(str, result)))
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == "__main__":
    main(path_input, path_output)
