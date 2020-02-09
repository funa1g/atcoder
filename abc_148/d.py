import sys

length = int(input())
bricks = input().split(' ')

counter = 0
top = 0
for i, brick in enumerate(bricks):
    if top+1 == int(brick):
        top += 1
    else:
        counter += 1
if top == 0:
    counter = -1
print(counter)
