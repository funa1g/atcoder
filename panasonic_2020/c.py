from math import sqrt

val = input().split(' ')
a = int(val[0])
b = int(val[1])
c = int(val[2])

# TODO このままだと、丸め桁数分間違いが発生する可能性がある
diff = sqrt(c) - sqrt(a) - sqrt(b)
result = 'Yes' if diff > 0 else 'No'
print(result)
