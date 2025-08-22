import sys
from collections import deque

N,K=map(int,sys.stdin.readline().rstrip().split(' '))
dist=[-1 for i in range(200000)]
dist[N]=0
dequee=deque()
dequee.append(N)

while(dequee):
    tmp=dequee.popleft()

    if(tmp==K):
        print(dist[K])
        break
    
    #2배 위치로 가기
    if(0<=2*tmp<200000 and dist[2*tmp]==-1):
        dist[2*tmp]=dist[tmp]
        dequee.append(2*tmp)

    #뒤로 가기
    if(0<=tmp-1<200000 and dist[tmp-1]==-1):
        dist[tmp-1]=dist[tmp]+1
        dequee.append(tmp-1)

    #앞으로 가기
    if(0<=tmp+1<200000 and dist[tmp+1]==-1):
        dist[tmp+1]=dist[tmp]+1
        dequee.append(tmp+1)