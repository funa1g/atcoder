def min_shop(time, shops):
    min_time = 1000000000
    for i, shop in enumerate(shops):
        t = shop[0] * time + shop[1]
        if t < min_time:
            min_time = t
            min_index = i
        elif t == min_time:
            if shop[0] > shops[min_index][0]:
                min_time = t
                min_index = i            
    if min_index or min_index == 0:
        shops.pop(min_index)
    return min_time


val = input().split(' ')
n = int(val[0])
t = int(val[1])
limit = t + 0.5

shops = []
for i in range(n):
    shops.append([int(shop) for shop in input().split(' ')])

time = 0
counter = 0
shopping = 0

while(time < limit):
    counter += 1
    if counter % 2 == 1:
        if counter != 1:
            shopping += 1
        if len(shops) == 0:
            break
        time += 1
    else:
        min_time = min_shop(time, shops)
        time += min_time
        
print(shopping)
