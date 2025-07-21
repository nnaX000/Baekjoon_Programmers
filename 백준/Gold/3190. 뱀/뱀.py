import sys
from collections import deque

head=[1,1]
answer=0
apple=set()
directions={}
current=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]

N=int(sys.stdin.readline().rstrip())
K=int(sys.stdin.readline().rstrip())

trace=deque()

trace.append([1,1])

for i in range(K):
    tmp=tuple(map(int,sys.stdin.readline().rstrip().split(' ')))
    apple.add(tmp)

L=int(sys.stdin.readline().rstrip())

for i in range(L):
    second, direction=sys.stdin.readline().rstrip().split(' ')
    directions[int(second)]=direction

while(True):
    head[0]+=dx[current]
    head[1]+=dy[current]
    answer+=1

    if(head[0]<1 or head[0]>N or head[1]<1 or head[1]>N):
        break

    if([head[0],head[1]] in trace):
        break
    
    trace.append([head[0],head[1]])

    if(tuple(head) in apple):
        apple.remove(tuple(head))
    else:
        trace.popleft()

    if(answer in directions.keys()):
        if(directions[answer]=="L"):
            current-=1
            if(current<0):
                current=3
        else:
            current+=1
            if(current>3):
                current=0

print(answer)