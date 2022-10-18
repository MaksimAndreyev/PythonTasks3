k = int(input('Введите число: '))
a = [0, 1]
if k == 0:
    print(0)
elif k == 1:
    print('1 0 1')
for i in range(1, k):
    a.append(a[i] + a[i-1])
for i in range(len(a)-1, 0, -1):
    if i % 2 == 0:
        print(-a[i], end=' ')
    else:
        print(a[i], end=' ')
print(*a)
