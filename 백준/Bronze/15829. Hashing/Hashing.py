import sys
from collections import defaultdict

alpha=defaultdict(int)

#r은 31, M은 1234567891

L_len=int(sys.stdin.readline().rstrip())
L=sys.stdin.readline().rstrip()

num=1
answer=0

for i in range(97,123):
    alpha[chr(i)]=num
    num+=1

for idx,i in enumerate(L):
    num=alpha[i]
    answer+=((num)*(31**idx))

answer%=1234567891

print(answer)