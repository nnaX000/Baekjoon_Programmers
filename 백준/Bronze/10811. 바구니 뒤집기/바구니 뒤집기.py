import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

array=[0]*(N+1)

for i in range(1,len(array)):
    array[i]=i

for i in range(M):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    array[x:y+1]=reversed(array[x:y+1])

for i in range(1,len(array)):
    print(array[i],end=" ")