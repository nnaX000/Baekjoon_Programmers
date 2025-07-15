import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

array=[0]*(N+1)

for i in range(1,N+1):
    array[i]=i

for i in range(M):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    array[x],array[y]=array[y],array[x]

for i in range(1,N+1):
    print(array[i],end=" ")