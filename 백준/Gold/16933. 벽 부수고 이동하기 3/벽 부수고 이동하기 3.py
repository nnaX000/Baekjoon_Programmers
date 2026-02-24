import sys
from collections import deque

input=sys.stdin.readline

N,M,K=map(int,input().split())

maps=[list(map(int,input().rstrip())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[[False for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

#(0,0) -> (N-1,M-1)
#count가 홀수면 밤, 짝수면 낮으로 관리하면 안되는게.. 제자리에 머무르는 경우도 있음

def bfs(x,y):
    dq=deque()
    dq.append((x,y,1,0,0)) # x,y,거리,벽 뿌순 횟수, night(1) or day(0)

    while(dq):
        cx,cy,cost,count,day=dq.popleft()
        #print(cx,cy,cost,count,day)

        if(cx==N-1 and cy==M-1):
            print(cost)
            sys.exit(0)

        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if(0<=nx<N and 0<=ny<M):
                if(maps[nx][ny]==1):
                    if(count<K):
                        if(not visited[nx][ny][count+1]):
                            if(day==0):
                                visited[nx][ny][count+1]=True
                                #print(cx,cy,cost,count,day,"일때,",nx,ny,cost+1,count+1,1)
                                dq.append((nx,ny,cost+1,count+1,1))
                            else:
                                dq.append((cx,cy,cost+1,count,day^1))
                else:
                    if(not visited[nx][ny][count]):
                        visited[nx][ny][count]=True
                        #print(cx,cy,cost,count,day,"일때,",nx,ny,cost+1,count,day^1)
                        dq.append((nx,ny,cost+1,count,day^1))

visited[0][0][0] = True
bfs(0,0)
print(-1)