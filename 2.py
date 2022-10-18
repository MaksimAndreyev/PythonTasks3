a = list(map(int, input('Введите список через пробел: ').split()))
j = len(a) - 1
for i in range(len(a) // 2):
    print(a[i] * a[j], end=' ')
    j -= 1
if len(a) % 2 != 0:
    print(a[len(a) // 2] ** 2)
