import sys
from collections import deque

#사다리를 이용하면 원래 있던 칸 번호보다 크고 뱀을 이용하면 원래 있던 칸보다 작아진다.

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

dequee=deque()

ladder={}

for i in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    ladder[x]=y

snake={}

for i in range(M):
    u,v=map(int,sys.stdin.readline().rstrip().split(' '))
    snake[u]=v

visited=[10000000 for i in range(101)]
visited[1]=0
num=0

dequee.append(1)

while(dequee):
    tmp=dequee.popleft()
    cost=visited[tmp]

    for i in range(1,7):
        if(1<=tmp+i<101 and visited[tmp+i]==10000000):
            nb=tmp+i
            visited[nb]=cost+1

            while((nb in ladder) or (nb in snake)):

                if(nb in ladder):
                    nb=ladder[nb]
                    visited[nb]=min(visited[nb],cost+1)

                if(nb in snake):
                    nb=snake[nb]
                    visited[nb]=min(visited[nb],cost+1)

            dequee.append(nb)

    if(visited[100]!= 10000000):
        print(visited[100])
        break