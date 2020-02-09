h = int(input().strip())

for i in range(41):
    if 2**(i+1) > h and h >= 2**i:
        n = i + 1
        break
print(2**n - 1)
