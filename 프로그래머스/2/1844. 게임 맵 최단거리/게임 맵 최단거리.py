from collections import deque
def solution(maps):
    answer = 1
    dequee=deque()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    m=len(maps)
    n=len(maps[0])
    dequee.append((0,0))
    while(dequee):
        answer+=1
        size=len(dequee)
        for i in range(size):
            tmp=dequee.popleft()
            for j in range(len(dy)):
                targetX=tmp[0]+dx[j]
                targetY=tmp[1]+dy[j]
                if(targetX<0 or targetY<0 or targetX>=m or targetY>=n):
                    continue
                if(maps[targetX][targetY]==0):
                    continue
                if(maps[targetX][targetY]==1):
                    if(targetX==m-1 and targetY==n-1):
                        return answer
                    maps[targetX][targetY]=0
                    dequee.append((targetX,targetY))
    return -1