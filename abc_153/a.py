val = input().split(' ')
h = int(val[0])
a = int(val[1])

for i in range(1, 10001):
    h -= a
    if h <= 0:
        n = i
        break

print(i)
