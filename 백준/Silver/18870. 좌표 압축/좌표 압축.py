import sys
from collections import defaultdict

input=sys.stdin.readline

N=int(input())
X=list(map(int,input().split()))
num=defaultdict(int)

a_X=sorted(X)
idx=0

for i in range(N):
    if(a_X[i] not in num):
        num[a_X[i]]=idx
        idx+=1

for i in X:
    print(num[i],end=" ")