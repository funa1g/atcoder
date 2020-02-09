from operator import add
from functools import reduce

val = input().split(' ')
h = int(val[0])
k = int(val[1])
h = sorted([int(i) for i in input().split(' ')])

remains = h[:-k] if k > 0 else h
print(reduce(add, remains) if len(remains) > 0 else 0)
