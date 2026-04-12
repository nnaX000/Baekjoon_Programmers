import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

position=list(map(int,input().split()))

dq=deque()

answer=0

for i in range(1,N+1):
    dq.append(i)

for i in position:
    idx=dq.index(i)

    if(idx>len(dq)//2):
        for _ in range(len(dq)-idx):
            tmp=dq.pop()
            dq.appendleft(tmp)
            answer+=1
    else:
        for _ in range(idx):
            tmp=dq.popleft()
            dq.append(tmp)
            answer+=1

    dq.popleft()

print(answer)