from collections import defaultdict
from lab6.utils import open_file, write_file, memory_usage_process, print_input_output
import time
path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def process_elections(candidates_input):
    votes = defaultdict(int)

    for line in candidates_input:
        candidate, vote_count = line.split()
        votes[candidate] += int(vote_count)

    sorted_candidates = sorted(votes.items())

    result = []
    for candidate, votes in sorted_candidates:
        result.append(f'{candidate} {votes}')

    return result


def main(path_input, path_output):
    candidates = open_file(path_input)
    inputs = ''.join(candidates)

    memory_before = memory_usage_process()
    time_st = time.perf_counter()
    result = '\n'.join(process_elections(candidates))
    time_end = time.perf_counter() - time_st
    memory_after = memory_usage_process()

    write_file(result, path_output)
    print_input_output(inputs=inputs, result=result)
    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)