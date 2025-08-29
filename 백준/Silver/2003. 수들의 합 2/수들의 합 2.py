import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

sum_value=[0 for i in range(N+1)]
tmp=0
answer=0

for i in range(N):
    tmp+=A[i]
    sum_value[i+1]=tmp

for i in range(N+1):
    for j in range(0,i):
        if(sum_value[i]-sum_value[j]==M):
            answer+=1
print(answer)