from lab7.utils import write_file, open_file, print_input_output, measuring

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def find_min_operations(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    path = []
    current = n
    while current > 1:
        path.append(str(current))
        if current % 3 == 0 and dp[current] == dp[current // 3] + 1:
            current //= 3
        elif current % 2 == 0 and dp[current] == dp[current // 2] + 1:
            current //= 2
        else:
            current -= 1
    path.append(str(1))
    return [str(dp[n]) + "\n", (" ").join(path[::-1])]


def main(path_input, path_output):
    with open(path_input, "r") as file:
        n = int(file.readline())
    inputs = f"{n}"
    k, path = find_min_operations(n)
    result = f"{k}" + " ".join(map(str, path))
    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    measuring(find_min_operations, n)


if __name__ == '__main__':
    main(path_input, path_output)

