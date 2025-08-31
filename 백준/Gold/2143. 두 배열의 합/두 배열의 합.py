import sys
from collections import defaultdict

T=int(sys.stdin.readline().rstrip())
n=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
m=int(sys.stdin.readline().rstrip())
B=list(map(int,sys.stdin.readline().rstrip().split(' ')))

A_sum_value=[0 for i in range(n+1)]
B_sum_value=[0 for i in range(m+1)]

A_cnt=defaultdict(int)
B_cnt=defaultdict(int)

answer=0

tmp=0

for i in range(n):
    tmp+=A[i]
    A_sum_value[i+1]=tmp

tmp=0

for i in range(m):
    tmp+=B[i]
    B_sum_value[i+1]=tmp

for i in range(n+1):
    for j in range(0,i):
        A_cnt[A_sum_value[i]-A_sum_value[j]]+=1

for i in range(m+1):
    for j in range(0,i):
        B_cnt[B_sum_value[i]-B_sum_value[j]]+=1

for key,value in A_cnt.items():
    answer+=value*(B_cnt.get(T-key,0))

print(answer)