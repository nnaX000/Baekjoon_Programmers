import sys

N,K=map(int,sys.stdin.readline().rstrip().split(' '))

bags=[]
weight=[0 for i in range(K+1)]
max_value=float('-inf')

for i in range(N):
    w,v = map(int,sys.stdin.readline().rstrip().split(' ')) #무게, 가치
    for j in range(K,w-1,-1):
        weight[j]=max(weight[j],weight[j-w]+v)

print(max(weight))