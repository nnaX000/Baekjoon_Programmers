import sys
from collections import deque

N,K=map(int,sys.stdin.readline().rstrip().split(' '))

path=[-1 for i in range(100001)]
dequee=deque()
time=0
dequee.append([N,time])
answer=[]

while(dequee):
    tmp=dequee.popleft()

    if(tmp[0]==K):
        print(tmp[1])
        target=K
        answer.append(target)
        for i in range(tmp[1]):
            answer.append(path[target])
            target=path[target]
        answer.reverse()
        print(*answer)
        break
    
    if(0<=tmp[0]-1<=100000 and path[tmp[0]-1]==-1):
        path[tmp[0]-1]=tmp[0]
        dequee.append([tmp[0]-1,tmp[1]+1])

    if(0<=tmp[0]+1<=100000 and path[tmp[0]+1]==-1):
        path[tmp[0]+1]=tmp[0]
        dequee.append([tmp[0]+1,tmp[1]+1])

    if(0<=tmp[0]*2<=100000 and path[tmp[0]*2]==-1):
        path[tmp[0]*2]=tmp[0]
        dequee.append([tmp[0]*2,tmp[1]+1])