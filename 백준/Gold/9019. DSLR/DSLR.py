import sys
from collections import deque

input=sys.stdin.readline

T=int(input())

how=["" for i in range(10000)]
parent=[0 for i in range(10000)]
visited=[0 for i in range(10000)]

for i in range(1,T+1):
    A,B=map(int,input().split())

    q=deque()

    q.append((A))

    if(visited[A]!=i):
        visited[A]=i

    while(q):
        x=q.popleft()

        if(x==B):
            break

        tmp=(x*2)%10000

        if(visited[tmp]!=i):
            q.append(tmp)
            how[tmp]="D"
            parent[tmp]=x
            visited[tmp]=i

        tmp = 9999 if x == 0 else x - 1

        if(visited[tmp]!=i):
            q.append(tmp)
            how[tmp]="S"
            parent[tmp]=x
            visited[tmp]=i

        tmp = (x % 1000) * 10 + (x // 1000)

        if(visited[tmp]!=i):
            q.append(tmp)
            how[tmp]="L"
            parent[tmp]=x
            visited[tmp]=i

        tmp = (x % 10) * 1000 + (x // 10)

        if(visited[tmp]!=i):
            q.append(tmp)
            how[tmp]="R"
            parent[tmp]=x
            visited[tmp]=i

    answer=[]
    cur=B

    while(cur!=A):
        answer.append(how[cur])
        cur=parent[cur]

    print(''.join(reversed(answer)))