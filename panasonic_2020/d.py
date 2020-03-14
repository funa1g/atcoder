# 終わってからできた

n = int(input())

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
# results = []
# if n == 1:
#     results = ["a"]
# elif n == 2:
#     results = ["aa", "ab"]
# elif n == 3:
#     results = ["aaa", "aab", "aba", "abb", "abc"]
# elif n == 4:
#     results = ["aaaa", "aaab", "aaba", "aabb", "aabc", "abaa", "abab", "abac", "abba", "abbb", "abbc", "abca", "abcb", "abcc", "abcd"]

results = []
for i in range(n):
    if i == 0:
        results.append(["a"])
    else:
        standards = []
        for result in results[i-1]:
            abcs = list(set(result))
            abcs.append(abc[len(abcs)])
            for a in abcs:
                standards.append(result + a)
        results.append(standards)

# for result in results:
for result in sorted(results[n-1]):
    print(result)
