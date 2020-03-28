val = input().split(' ')
n = int(val[0])
x = int(val[1])
y = int(val[2])

dists = {}
for i in range(1, n):
    dists[i] = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        len1 = j - i
        len2 = abs(j - y) + abs(x - i) + 1
        len3 = abs(y - i) + abs(j - x) + 1
        dist = len1 if len1 < len2 else len2
        dist = dist if dist < len3 else len3
        dists[dist] += 1

for i in range(1, n):
    print(dists[i])
