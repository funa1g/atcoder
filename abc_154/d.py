import numpy as np

n,k = map(int,input().split())



p_list = np.fromstring(input(),int,sep=' ')

cumulative_sum = np.zeros(n+1)
cumulative_sum[1:] = p_list.cumsum()

length_k_sum_list = cumulative_sum[k:] - cumulative_sum[0:-k]

e_max = length_k_sum_list.max()

print((e_max + k) / 2 )
