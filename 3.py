a = list(map(float, input('Введите список через пробел: ').split()))
mx = 0
mn = 1
for i in a:
    f = i % 1
    mx = max(f, mx)
    mn = min(f, mn)
print(mx - mn)
