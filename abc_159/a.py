val = input().split(' ')
n = int(val[0])
m = int(val[1])

result = n * (n-1) / 2 + m * (m-1) / 2

print(int(result))
