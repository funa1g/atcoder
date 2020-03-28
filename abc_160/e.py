val = input().split(' ')
x = int(val[0])
y = int(val[1])
a = int(val[2])
b = int(val[3])
c = int(val[4])
 
p_list = sorted([int(a) for a in input().split(' ')])
q_list = sorted([int(a) for a in input().split(' ')])
r_list = sorted([int(a) for a in input().split(' ')])
p_list.reverse()
q_list.reverse()
r_list.reverse()
 
xapples = p_list[0:x]
yapples = q_list[0:y]
zapples = r_list[0:x+y]
 
xapples.extend(yapples)
xapples.extend(zapples)
tmp_apples = sorted(xapples)
tmp_apples.reverse()
apples = tmp_apples[0:x+y]
print(sum(apples))
