import sys

N,K=map(int,sys.stdin.readline().rstrip().split(' '))

array=[[1 for i in range(N+1)] for j in range(K)]

for i in range(1,K):
    for j in range(1,N+1):
        array[i][j]=(array[i-1][j]+array[i][j-1])%1000000000

print(array[K-1][N]%1000000000)