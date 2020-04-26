import time

a = [1] * 100000000
result = 0
start = time.time()
for i in a:
    result += i
print(time.time() - start)
