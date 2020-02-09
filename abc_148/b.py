import sys

length = int(input())
strings = input().split(' ')
s = strings[0].strip()
t = strings[1].strip()

st = ''
for i in range(length):
  st += s[i] + t[i]

print(st)

