import collections

n = int(input())
a = [int(i) for i in input().split(' ')]
c = collections.Counter(a)
counts = {}
all_sum = 0
for k, v in c.items():
    val = v * (v-1) / 2
    counts[k] = val
    all_sum += val

for i in range(n):
    k = a[i]
    count = c[k] - 1
    val = counts[k]
    print(int(all_sum - val + count * (count - 1) / 2))
