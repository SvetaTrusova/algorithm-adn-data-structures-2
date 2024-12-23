from lab2.utils import open_file, write_file, measuring, print_input_output


path_input = '../txtf/input.txt'
path_output = '../txtf/output.txt'


def merge(left, right):
    if left[-1] <= right[0]:
        return left + right

    list_merged = list()
    left_i = right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                list_merged.append(left[left_i])
                left_i += 1
            else:
                list_merged.append(right[right_i])
                right_i += 1

    while left_i < len(left):
        list_merged.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        list_merged.append(right[right_i])
        right_i += 1

    return list_merged


def merge_sort(list_arr):
    if len(list_arr) <= 1:
        return list_arr

    middle = len(list_arr) // 2
    left_list = merge_sort(list_arr[:middle])
    right_list = merge_sort(list_arr[middle:])
    return merge(left_list, right_list)


def main(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums))
    result = ' '.join(map(str, merge_sort(nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(merge_sort, nums)


if __name__ == "__main__":
    main(path_input, path_output)
