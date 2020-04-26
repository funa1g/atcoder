def calc(sentence, result):
    if len(sentence) <= 4:
        return
    if int(sentence) % 2019 == 0:
        result += 1
    calc(sentence[:-1], result)
    calc(sentence[1:], result)


s = input()
n = len(s)
result = 0
calc(s, result)
print(result)

# for i in range(5, n):
#     for j in range(n - i + 1):
#         sub_s = s[j:j+i]
#         if int(sub_s) % 2019 == 0:
#             result += 1
# print(result)
