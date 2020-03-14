val = input().split(' ')
h = int(val[0])
w = int(val[1])

square_num = h * w
result = square_num / 2
if h == 1 or w == 1:
    result = 1
elif square_num % 2 == 1:
    result += 0.5
print(int(result))
