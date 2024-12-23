from lab7.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def coins_function(money, coins):
    table = [float('inf')] * (money + 1)
    table[0] = 0
    for coin in coins:
        for x in range(coin, money + 1):
            table[x] = min(table[x], table[x - coin] + 1)
    return table[money] if table[money] != float('inf') else -1


def main(input_file, output_file):
    money, k, coins = open_file(input_file)
    inputs = str(money) + ' ' + str(k) + '\n' + ' '.join(map(str, coins))
    result = str(coins_function(money, coins))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(coins_function, money, coins)


if __name__ == '__main__':
    main(PATH_INPUT, PATH_OUTPUT)
