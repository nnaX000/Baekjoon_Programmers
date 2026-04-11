import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
tower=list(map(int,input().split()))

# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력

dq=deque()
answer=[0 for _ in range(N)]

for i in range(N):
    while dq and dq[-1][1] < tower[i] :
        dq.pop()

    if dq:
        answer[i]=dq[-1][0]+1
    else:
        answer[i]=0

    dq.append((i,tower[i]))

print(*answer)