s = input()
q = int(input())

is_reverse = False
front_queue = []
back_queue = []
for i in range(q):
    t = input()
    if t == "1":
        is_reverse = not is_reverse
    else:
        t2, f, c = t.split()
        if (f == "1" and not is_reverse) or (f == "2" and is_reverse):
            front_queue.append(c)
        else:
            back_queue.append(c)

result = ""
if is_reverse:
    result = "".join(reversed(back_queue)) + s[::-1] + "".join(front_queue)
else:
    result = "".join(reversed(front_queue)) + s + "".join(back_queue)
print(result)
