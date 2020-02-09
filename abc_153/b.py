val = input().split(' ')
h = int(val[0])
n = int(val[1])
skills = [int(i) for i in input().split(' ')]

able = 'No'
for i in skills:
    h -= i
    if h <= 0:
        able = 'Yes'
        break

print(able)
