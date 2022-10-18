a = list(map(int, input('Введите список через пробел: ').split()))
s = 0
for i in range(1, len(a), 2):
    s += a[i]
print(s)
