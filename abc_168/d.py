def calc(path, dist):
    for r in roads[path]:
        temp = distances[int(r)]
        if temp == 0 or dist < temp:
            distances[int(r)] = dist
            guides[int(r)] = path
            calc(r, dist + 1)


n, m = map(int, input().split())
roads = {}
for i in range(m):
    a, b = input().split()
    if b != "1":
        if a in roads:
            roads[a].append(b)
        else:
            roads[a] = [b]
    if a != "1":
        if b in roads:
            roads[b].append(a)
        else:
            roads[b] = [a]

distances = [0] * (n + 1)
guides = [0] * (n + 1)

calc("1", 1)

distances = distances[2:]
guides = guides[2:]

if 0 in distances:
    print("No")
else:
    print("Yes")
    for guide in guides:
        print(guide)
