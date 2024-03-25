#1 익은 토마토 0 익지 않은 토마토 -1 토마토가 들어있지 않음
#출력: 저장될 때부터 모든 토마토가 익어있는 상황 : 0 토마토가 모두 익지 못하는 상황:-1
import sys
from collections import deque
def BFS(dequee,array,garo,sero,zerocount):
    switch=0
    count=0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while(dequee):
        size=len(dequee)
        count+=1
        for i in range(size):
            stand=dequee.popleft()
            for j in range(4):
                targetX=stand[0]+dx[j]
                targetY=stand[1]+dy[j]
                if(targetX<0 or targetY<0 or targetX>=sero or targetY>=garo):
                    continue
                if(array[targetX][targetY]==0):
                    switch+=1
                    array[targetX][targetY]=1
                    dequee.append([targetX,targetY])
        if(switch==zerocount):
            return count
    #print("switch",switch,"zerocount",zerocount)
    if(len(dequee)==0 and switch<zerocount):
        return -1
dequee=deque()
garo,sero=map(int,sys.stdin.readline().split(' '))
array=[[0 for i in range(garo)]for j in range(sero)]
empty=0
onecount=0
zerocount=0
for i in range(sero):
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    array[i]=tmp
    for idx,j in enumerate(tmp):
        if(j==1):
            dequee.append([i,idx])
            onecount+=1
        if(j==-1):
            empty+=1
        if(j==0):
            zerocount+=1
if(onecount==(garo*sero-empty)):
    print(0)
else:
    answer=BFS(dequee,array,garo,sero,zerocount)
    print(answer)