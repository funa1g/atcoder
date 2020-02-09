import sys

def is_even(num):
    return num % 2 == 0

val = input()
if int(val) % 2 == 1:
    print(0)
else:
    counter = 0
    digits = len(val)
    for i, num in enumerate(val[::-1]):
        if i+1 != digits:
            counter += i * 9
        else:
            counter += i * int(num)
    print(counter)
