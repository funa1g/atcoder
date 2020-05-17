n = input()

last_str = n[-1]
result = "hon"
if last_str == "3":
    result = "bon"
elif last_str in ["0", "1", "6", "8"]:
    result = "pon"
print(result)
