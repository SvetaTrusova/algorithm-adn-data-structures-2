a, b = input().split()
a = int(a)
b = int(b)
if -10**9 <= a <= 10**9 and -10**9 <= a <= 10**9:
    print(a + b**2)
else:
    print(f'Числа a, b должны находиться в диапазоне от -10**9 до 10**9. Введите ещё раз')
    a = int(input())
    b = int(input())
    print(a + b**2)
