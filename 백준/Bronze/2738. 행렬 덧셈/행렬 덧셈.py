import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

one=[[0 for i in range(M)] for j in range(N*2)]

for i in range(N*2):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    one[i]=tmp

for i in range(N):
    for j in range(M):
        one[i][j]=one[i][j]+one[i+N][j]

for i in range(N):
    for j in range(M):
        print(one[i][j],end=" ")
    print()