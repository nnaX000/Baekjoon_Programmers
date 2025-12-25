import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

array=[0]
array.extend(list(map(int,sys.stdin.readline().rstrip().split(' '))))

for i in range(2,len(array)):
    array[i]=array[i-1]+array[i]

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))
    print(array[b]-array[a-1])