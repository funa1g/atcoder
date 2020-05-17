k = int(input())
s = input()

result = s
if len(s) > k:
    result = s[:k] + "..."

print(result)
