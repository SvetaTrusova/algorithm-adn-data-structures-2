from lab6.utils import write_file, open_file, print_input_output, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def edit_distance(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1],
                               dp[i][j - 1],
                               dp[i - 1][j]) + 1

    operations = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(f"change {a[i - 1]} {b[j - 1]}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"del {a[i - 1]}")
            i -= 1
        else:
            operations.append(f"add {b[j - 1]}")
            j -= 1

    operations.reverse()

    return dp[n][m], operations


def main(path_input, path_output):
    a, b = open_file(path_input)

    inputs = f"{a.strip()}\n{b.strip()}\n"

    memory_before = memory_usage_process()
    time_st = time.perf_counter()

    dist, operations = edit_distance(a.strip(), b.strip())

    result = f"{dist}\n" + "\n".join(operations)

    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
