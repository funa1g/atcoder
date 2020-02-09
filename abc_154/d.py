from decimal import Decimal

val = input().split(' ')
n = int(val[0])
k = int(val[1])

p_list = [ int(p) for p in input().split(' ')]

e_max = 0

for i in range(n - k + 1):
    temp = sum(p_list[i:k+i])
    if e_max < temp:
        e_max = temp

print(Decimal(e_max + k)/Decimal(2))
