from math import ceil
a, b, c, d = map(int, input().split())
t_count = ceil(c / b)
a_count = ceil(a / d)
result = "Yes" if t_count <= a_count else "No"
print(result)
