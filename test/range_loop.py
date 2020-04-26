import time

iter_num = 100000000
a = [1] * iter_num
result = 0
start = time.time()
for i in range(iter_num):
    result += a[i]
print(time.time() - start)
