s = input()
n = len(s)

front = s[0:int((n-1)/2)]
back = s[int((n+1)/2):]
if front == back[::-1] and front == back:
    print("Yes")
else:
    print("No")
