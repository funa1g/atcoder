val = input().split(' ')
a = int(val[0])
b = int(val[1])
m = int(val[2])

alist = [int(a) for a in input().split(' ')]
blist = [int(b) for b in input().split(' ')]

min_price = sorted(alist)[0] + sorted(blist)[0]

for i in range(m):
    discount = [int(m) for m in input().split(' ')]
    price = alist[discount[0] - 1] + blist[discount[1] - 1] - discount[2]
    if price < min_price:
        min_price = price

print(min_price)
