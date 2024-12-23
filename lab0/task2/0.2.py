import time
t_start = time.perf_counter()
with open('input 0.2') as f:
    n = int(f.readline())
    max = 45
    min = 0
    if n < min or n > max:
        print('Число должно находиться в диапазоне от 0 до 45. Введите ещё раз')
        n = int(input())
if n == 0:
    with open('output 0.2', 'w') as f:
        f.write('0')
elif n == 1:
    with open('output 0.2', 'w') as f:
        f.write('1')
else:
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    with open('output 0.2', 'w') as f:
        f.write(str(b))
print(time.perf_counter() - t_start)



