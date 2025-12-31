import sys
from collections import deque

input=sys.stdin.readline

T=int(input())

for i in range(T):
    A,B=map(int,input().split())

    q=deque()

    q.append((A,""))
    visited=set()
    visited.add(A)

    while(q):
        x,command=q.popleft()

        if(x==B):
            print(command)
            break

        tmp=x*2
        if(tmp>9999):
            tmp%=10000

        if(tmp not in visited):
            q.append((tmp,command+"D"))
            visited.add(tmp)

        if(x==0):
            tmp=9999
        else:
            tmp=x-1

        if(tmp not in visited):
            q.append((tmp,command+"S"))
            visited.add(tmp)

        tmp = (x % 1000) * 10 + (x // 1000)

        if(tmp not in visited):
            q.append((tmp,command+"L"))
            visited.add(tmp)

        tmp = (x % 10) * 1000 + (x // 10)

        if(tmp not in visited):
            q.append((tmp,command+"R"))
            visited.add(tmp)