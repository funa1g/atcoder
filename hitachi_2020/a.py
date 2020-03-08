import re

s = input()

match = re.match(r"^(hi)+$", s)

result = "Yes" if match else "No"

print(result)
