from lab2.utils import read_input, write_output, normVid, memory_usage_process
import time

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def to_sort(arr):
    result = count_inversions(arr)
    return result


def merge_and_count(arr, temp_arr, left, right):
    """Функция для сортировки слиянием и подсчёта инверсий"""
    if left == right:
        return 0

    mid = (left + right) // 2
    inv_count = 0
    inv_count += merge_and_count(arr, temp_arr, left, mid)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
    inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    """Функция слияния двух отсортированных половин массива с подсчётом инверсий"""
    i = left  # Начало левой половины
    j = mid + 1  # Начало правой половины
    k = left  # Индекс для временного массива
    inv_count = 0

    # Слияние двух отсортированных половин
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Все элементы, оставшиеся в левой половине, больше arr[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы из левой половины
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из правой половины
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def count_inversions(arr):
    """Главная функция подсчёта инверсий"""
    n = len(arr)
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1)


def main(path_input, path_output):
    n, arr = read_input(path_input)
    print("Входные данные:")
    print(n)
    print(*arr)

    memory_before = memory_usage_process()

    time_st = time.perf_counter()
    result = count_inversions(arr)
    time_end = time.perf_counter() - time_st

    memory_after = memory_usage_process()

    print(f"Результат: \n{result}")

    write_output(str(result), path_output)

    print(f"Затраченная память: {memory_after - memory_before} Megabytes")
    print(f"Время выполнения: {time_end: .4f} секунд.")


if __name__ == '__main__':
    main(path_input, path_output)
