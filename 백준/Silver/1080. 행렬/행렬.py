import sys
from collections import deque

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

A=[]
B=[]

count=0

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(N):
    B.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(N-2):
    for j in range(M-2):
        if(A[i][j]!=B[i][j]):
            count+=1
            for l in range(i,i+3):
                for k in range(j,j+3):
                    A[l][k]^=1

if(A==B):
    print(count)
else:
    print(-1)