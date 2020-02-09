import sys

choices = [1,2,3]
for l in sys.stdin:
    choices.remove(int(l))

print(choices.pop())

