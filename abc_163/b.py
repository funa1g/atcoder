n, m = map(int, input().split())

a_list = map(int, input().split())

result = n - sum(a_list)
if result < 0:
    print(-1)
else:
    print(result)
