n = int(input())
a_list = map(int, input().split())

sub_nums = [0] * n
for a in a_list:
    sub_nums[a - 1] += 1

print("\n".join(map(str, sub_nums)))
