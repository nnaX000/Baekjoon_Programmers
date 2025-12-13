import sys

def main():

    N,M=map(int,sys.stdin.readline().rstrip().split(' '))

    castle=[list(sys.stdin.readline().rstrip()) for i in range(M)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited=[[False for i in range(N)] for j in range(M)]
    count=0
    answer=[0,0]

    def dfs(x,y,color):
        nonlocal visited
        nonlocal count

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<M and 0<=ny<N and castle[nx][ny]==color and not visited[nx][ny]):
                visited[nx][ny]=True
                count+=1
                dfs(nx,ny,color)

    for i in range(M):
        for j in range(N):
            if(not visited[i][j]):
                count=1
                visited[i][j]=True

                dfs(i,j,castle[i][j])

                if(castle[i][j]=="W"):
                    answer[0]+=count**2
                else:
                    answer[1]+=count**2

    print(*answer)


if __name__ == "__main__":
    main()