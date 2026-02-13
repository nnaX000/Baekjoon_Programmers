import sys
from collections import defaultdict,deque

input=sys.stdin.readline

N,K=map(int,input().split())
a=list(map(int,input().split()))

sum_value=defaultdict(int)
sequence=defaultdict(deque)
start=0

answer=float('-inf')

for i in range(N):
    if(sum_value[a[i]]<K):
        sum_value[a[i]]+=1
        sequence[a[i]].append(i)
        answer=max(answer,i-start+1)
    else:
        tmp=sequence[a[i]][0]

        if(tmp>=start):
            for j in range(start,tmp+1):
                sum_value[a[j]]-=1
                sequence[a[j]].popleft()

            start=tmp+1

        sequence[a[i]].append(i)
        sum_value[a[i]]+=1
        answer=max(answer,i-start+1)

print(answer)