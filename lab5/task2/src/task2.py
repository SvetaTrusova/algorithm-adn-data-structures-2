from lab2.utils import read_input, write_output, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def calculate_tree_height(n, parents):
    children = [[] for _ in range(n)]
    root = None

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    def dfs(node):
        stack = [(node, 1)]
        max_depth = 0

        while stack:
            current, depth = stack.pop()
            max_depth = max(max_depth, depth)
            for child in children[current]:
                stack.append((child, depth + 1))

        return max_depth

    return dfs(root)


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print(f"Входные данные: \n{n}")
    print(*arr)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = calculate_tree_height(n, arr)
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    print(f"Результат:\n{result}")
    write_output(str(result), path_output)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
