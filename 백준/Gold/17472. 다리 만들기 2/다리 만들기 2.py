import sys
from collections import deque,defaultdict
import heapq

input=sys.stdin.readline

N,M=map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(N)]
roads=defaultdict(lambda : defaultdict(int))

heap=[]
heapq.heapify(heap)

#섬 x에서 섬y로 가는 모든 경로 구하기 -> 최단경로만 남겨놓고 모두 삭제
#섬끼리 모든 관계를 구해놓고 섬개수-1, 섬개수 만큼 조합 돌리기
#해당 조합에서 모든 섬 탐색가능한지 체크하고 가능하면 답 업데이트, 아니면 버리기

dx=[-1,1,0,0,0]
dy=[0,0,-1,1,0]

def bfs(a,b):
    global maps
    global num

    dq=deque()
    dq.append((a,b))
    maps[a][b]=num

    while(dq):
       x,y = dq.popleft()

       for i in range(4):
           nx=x+dx[i]
           ny=y+dy[i]

           if(0<=nx<N and 0<=ny<M and maps[nx][ny]==1):
               maps[nx][ny]=num
               dq.append((nx,ny))

def border(a,b):
    global stand

    dq=deque()
    dq.append((a,b)) #x,y

    while(dq):
        x,y=dq.popleft()

        for i in range(5):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and maps[nx][ny]==stand):
                t_x=nx
                t_y=ny
                for j in range(4):
                    nx=t_x+dx[j]
                    ny=t_y+dy[j]

                    if(0<=nx<N and 0<=ny<M and maps[nx][ny]==0):
                        path(nx,ny,j,stand)

def path(x,y,di,stand):
    nx=x
    ny=y
    cost=1

    while(True):
        nx+=dx[di]
        ny+=dy[di]

        if(not(0<=nx<N and 0<=ny<M)):
            break

        if(maps[nx][ny]==0):
            cost+=1
        
        if(maps[nx][ny]!=0):
            if(cost>=2):
                if(maps[nx][ny] in roads[stand]):
                    roads[stand][maps[nx][ny]]=min(cost,roads[stand][maps[nx][ny]])
                else:
                    roads[stand][maps[nx][ny]]=cost

                if(stand in roads[maps[nx][ny]]):
                    roads[maps[nx][ny]][stand]=min(cost,roads[maps[nx][ny]][stand])
                else:
                    roads[maps[nx][ny]][stand]=cost

                break
            else:
                break

def prim():
    global island_cnt

    heap=[]
    visited=[False for _ in range(num+1)]
    picked=0
    answer=0
    heapq.heapify(heap)
    heapq.heappush(heap,(0,2)) #cost,node

    while(heap and picked<island_cnt):
        c,n=heapq.heappop(heap)
        if(visited[n]):
            continue
        visited[n]=True
        answer+=c
        picked+=1

        for i in range(len(adjust[n])):
            v,k=adjust[n][i][0],adjust[n][i][1]

            if(not visited[k]):
                heapq.heappush(heap,(v,k))

    return answer if picked==island_cnt else -1

num=2
for i in range(N):
    for j in range(M):
        if(maps[i][j]==1):
            bfs(i,j)
            num+=1

adjust=[[] for _ in range(num+1)]

for i in range(N):
    for j in range(M):
        if(maps[i][j]!=0):
            stand=maps[i][j]
            border(i,j)

for key,value in roads.items():
    for k,v in value.items():
        adjust[key].append([v,k]) # 거리, 목적지

island_cnt=num-2
print(prim())