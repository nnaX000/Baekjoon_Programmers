import sys
from collections import deque,defaultdict

T=int(sys.stdin.readline().rstrip())

# .은 빈공간
# *은 벽
# $은 상근이가 훔쳐야되는 문서
# 대문자가 문, 소문자가 열쇠

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(T):
    h,w=map(int,sys.stdin.readline().rstrip().split(' '))

    maps=[]
    for j in range(h):
        maps.append(list(sys.stdin.readline().rstrip()))

    keys=sys.stdin.readline().rstrip()
    dequee=deque()
    ram=defaultdict(set)
    answer=set()
    visited=[[False for j in range(w)] for k in range(h)]

    if(keys=="0"):
        keys=set()
    else:
        keys=set(list(keys))

    for j in range(h):
        for k in range(w):
            if(j==0 or j==h-1 or k==0 or k==w-1):
                if(maps[j][k]!="*"):
                    visited[j][k]=True
                    dequee.append((j,k))

    while(dequee):
        x,y=dequee.popleft()

        if(maps[x][y]=="$"):
            answer.add((x,y))
            for j in range(4):
                n_x=x+dx[j]
                n_y=y+dy[j]

                if(0<=n_x<h and 0<=n_y<w and maps[n_x][n_y]!="*" and not visited[n_x][n_y]):
                    visited[n_x][n_y]=True
                    dequee.append((n_x,n_y))

        if("A"<=maps[x][y]<="Z"):
            if(maps[x][y].lower() in keys):
                for j in range(4):
                    n_x=x+dx[j]
                    n_y=y+dy[j]

                    if(0<=n_x<h and 0<=n_y<w and maps[n_x][n_y]!="*" and not visited[n_x][n_y]):
                        visited[n_x][n_y]=True
                        dequee.append((n_x,n_y))
            else:
                ram[maps[x][y].lower()].add((x,y))
        elif("a"<=maps[x][y]<="z"):
            if(maps[x][y] not in keys):
                keys.add(maps[x][y])
                for a,b in ram[maps[x][y]]:
                    dequee.append((a,b))

                del ram[maps[x][y]]

            for j in range(4):
                    n_x=x+dx[j]
                    n_y=y+dy[j]

                    if(0<=n_x<h and 0<=n_y<w and maps[n_x][n_y]!="*" and not visited[n_x][n_y]):
                        visited[n_x][n_y]=True
                        dequee.append((n_x,n_y))
        elif(maps[x][y]=="."):
            for j in range(4):
                n_x=x+dx[j]
                n_y=y+dy[j]

                if(0<=n_x<h and 0<=n_y<w and maps[n_x][n_y]!="*" and not visited[n_x][n_y]):
                    visited[n_x][n_y]=True
                    dequee.append((n_x,n_y))

    print(len(answer))