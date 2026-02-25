import sys
from collections import defaultdict

input=sys.stdin.readline

N=int(input())
U=[]

for i in range(N):
    U.append(int(input()))

U.sort()
U_set=set(U)
sv=defaultdict(list)

for i in range(N):
    for j in range(i,N):
        sv[U[i]+U[j]].append([U[i],U[j]])

for i in range(N-1,-1,-1):
    for key,value in sv.items():
        ram=U[i]-key
        if(ram in U_set):
            print(U[i])
            sys.exit(0)