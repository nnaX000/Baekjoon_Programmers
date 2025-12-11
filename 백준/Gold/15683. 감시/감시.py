import sys
import copy

sys.setrecursionlimit(10**8)

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
office=[]

cctv=[[[[0,1]],[[0,-1]],[[-1,0]],[[1,0]]],[[[0,1],[0,-1]],[[1,0],[-1,0]]],[[[-1,0],[0,1]],[[0,1],[1,0]],[[0,-1],[1,0]],[[0,-1],[-1,0]]],[[[0,-1],[0,1],[-1,0]],[[0,1],[-1,0],[1,0]],[[1,0],[0,-1],[0,1]],[[1,0],[-1,0],[0,-1]]],[[[-1,0],[0,1],[0,-1],[1,0]]]]

for i in range(N):
    office.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

max_value=float('-inf')
answer=N*M

for i in range(N):
    for j in range(M):
        if(1<=office[i][j]<=6):
            answer-=1

def dfs(x,y,visited):
    global max_value

    for i in range(x,N):
        for j in range(y if i==x else 0,M):
            tmp_visited=set()
            if(1<=office[i][j]<6):
                tmp_visited=set()
                for k in range(len(cctv[office[i][j]-1])):
                    tmp_visited=set()

                    for l in range(len(cctv[office[i][j]-1][k])):#case 1,2,3
                        nx=i
                        ny=j
                        check=False

                        while(not check):
                            nx+=cctv[office[i][j]-1][k][l][0]
                            ny+=cctv[office[i][j]-1][k][l][1]

                            if(0<=nx<N and 0<=ny<M):
                                if(office[nx][ny]==6):
                                    check=True
                                elif(office[nx][ny]==0 and (nx,ny) not in visited):
                                    tmp_visited.add((nx,ny))
                            else:
                                check=True  

                    n_visited=copy.deepcopy(visited)
                    n_visited.update(tmp_visited)
                    dfs(i if j+1!=M else i+1, j+1 if j+1<M else 0,n_visited)

                return


    if(len(visited)>max_value):
        max_value=len(visited)
    return

visit=set()
dfs(0,0,visit)

print(answer-max_value)