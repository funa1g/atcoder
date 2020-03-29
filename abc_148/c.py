a, b = [int(a) for a in input().split(' ')]
m, n = a, b
temp = 1
while m % n != 0:
    temp = n
    n = m % n
    m = temp

result = a * b / n
print(int(result))
