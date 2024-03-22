from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split(' '))
miro=[[] for i in range(N)]
for i in range(N):
    tmp=list(map(int, sys.stdin.readline().strip()))
    miro[i]=tmp
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def BFS(miro):
    count=0
    dequee = deque()
    dequee.append([0, 0])
    while(dequee):
        size=len(dequee)
        count+=1
        for i in range(size):
            stand=dequee.popleft()
            miro[stand[0]][stand[1]]=0
            for j in range(4):
                targetX=stand[0]+dx[j]
                targetY=stand[1]+dy[j]
                if(targetX<0 or targetY<0 or targetX>=N or targetY>=M):
                    continue
                if(miro[targetX][targetY]==1):
                    dequee.append([targetX,targetY])
                    miro[targetX][targetY]=0
                    if(targetX==N-1 and targetY==M-1):
                        return count

answer=BFS(miro)
print(answer+1)
