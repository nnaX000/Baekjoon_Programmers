import sys
from collections import defaultdict

input=sys.stdin.readline

N=int(input())
U=[]

for i in range(N):
    U.append(int(input()))

U.sort()
U_set=set(U)
sv=set()

for i in range(N):
    for j in range(i,N):
        sv.add(U[i]+U[j])

for i in range(N-1,-1,-1):
    for value in sv:
        ram=U[i]-value
        if(ram in U_set):
            print(U[i])
            sys.exit(0)