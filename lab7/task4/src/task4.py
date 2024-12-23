from lab7.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def longest_common_subsequence(n, m, seq1, seq2):
    table = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n][m]


def main(input_file, output_file):
    n, a_list, m, b_list = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, a_list)) + '\n' + str(m) + '\n' + ' '.join(map(str, b_list))
    result = str(longest_common_subsequence(n, m, a_list, b_list))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(longest_common_subsequence, n, m, a_list, b_list)


if __name__ == '__main__':
    main(PATH_INPUT, PATH_OUTPUT)