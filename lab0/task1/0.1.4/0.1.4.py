with open('input 0.1.4') as f:
    a, b = map(int, f.readline().split())
    a = int(a)
    b = int(b)
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= a <= 10 ** 9:
        with open('output 0.1.4', 'w') as f:
            f.write(str(a + b ** 2))
    else:
        print('Числа a и b должны находиться в диапазоне от -10**9 до 10**9. Введите ещё раз')
        a, b = int(input()), int(input())
        with open('output 0.1.4', 'w') as f:
            f.write(str(a + b**2))
