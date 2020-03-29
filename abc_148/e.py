n = int(input())

result = 0
if n % 2 != 1:
    fexp = 0
    for i in range(1, n):
        fexp = 5 ** i * 2
        if fexp > n:
            break
        result += n // fexp

print(result)
