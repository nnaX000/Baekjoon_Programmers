import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

N,M=map(int,input().split())
cheeze=[list(map(int,input().split())) for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=0

# 실내온도 공기가 있는 칸 체크하기
def air(x,y):
    global cheeze
    global visited

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]==0 and not visited[nx][ny]):
            visited[nx][ny]=True
            cheeze[nx][ny]=2 # 실내 공기->2
            air(nx,ny)


visited[0][0] = True
cheeze[0][0] = 2
air(0,0)
tmp=[i[:] for i in cheeze]

while(True):
    melt=[]
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[0][0]=True
    cheeze[0][0]=0

    for i in range(N):
        for j in range(M):
            if(cheeze[i][j]==2):
                cheeze[i][j]=0

    air(0,0)

    for i in range(N):
        for j in range(M):
            if(cheeze[i][j]==1):
                cnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]

                    if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]==2):
                        cnt+=1

                if(cnt>=2):
                    melt.append([i,j])

    if(not melt):
        print(answer)
        break
    else:
        answer+=1

    for x,y in melt:
        cheeze[x][y]=0