x = int(input())

remainder = x % 500

fhj = int((x - remainder) / 500 * 1000)
fj = int(int(remainder / 5) * 5)
print(fhj + fj)
