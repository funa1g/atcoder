n = int(input())
a_list = map(int, input().split())

acts = {}
for i, a in enumerate(a_list):
    if a in acts:
        acts[a].append(i)
    else:
        acts[a] = [i]
sorted_acts = sorted(acts.items(), key=lambda x: x[0], reverse=True)

left_max = 0
right_max = n
result = 0
for key in sorted_acts.keys():
    tmp_dist = 0
    for a in sorted_acts[key]:
        right_dist = right_max - a
        left_dist = a - left_max
        dist = left_dist if left_dist > right_dist else right_dist
        if dist > tmp_dist:
            tmp_dist = dist
