import sys
from collections import deque,defaultdict

input=sys.stdin.readline

N=int(input())

dq=deque()
dq.append(1)

answer=[0 for _ in range(N+1)]
link=defaultdict(list)

for i in range(N-1):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

while(dq):
    tmp=dq.popleft()

    for value in link[tmp]:
        if(answer[value]==0):
            dq.append(value)
            answer[value]=tmp

for i in range(2,N+1):
    print(answer[i])