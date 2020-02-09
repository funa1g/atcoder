n = int(input())
a_list = sorted(input().split(" "))

result = "YES"
prev = ""
for a in a_list:
    if a == prev:
        result = "NO"
        break
    prev = a

print(result)
