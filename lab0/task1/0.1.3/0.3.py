with open('input 0.3') as f:
    a, b = map(int, f.readline().split())
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= a <= 10 ** 9:
        with open('output 0.3', 'w') as f:
            f.write(str(a + b))
    else:
        print('Числа a и b должны находиться в диапазоне от -10**9 до 10**9. Введите ещё раз')
        a, b = int(input()), int(input())
        with open('output 0.3', 'w') as f:
            f.write(str(a + b))
    
