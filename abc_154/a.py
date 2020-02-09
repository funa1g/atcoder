val = input().split(' ')
s = val[0]
t = val[1]

val = input().split(' ')
a = int(val[0])
b = int(val[1])

u = input()

if s == u:
    a -= 1
elif t == u:
    b -= 1

print("{} {}".format(a, b))
