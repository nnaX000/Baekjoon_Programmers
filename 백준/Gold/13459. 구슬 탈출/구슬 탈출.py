import sys
from collections import deque

#세로 N, 가로 M
#빨간 구슬을 구멍을 통해 빼내는 게임이고 파란 구슬이 들어가면 안된다
#왼쪽, 오른쪽, 위쪽, 아래쪽으로 굴린다

blue_x=0
blue_y=0
red_x=0
red_y=0
hole_x=0
hole_y=0

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
board=[]
dequee=deque()
visited=set()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if(board[i][j]=="O"):
            hole_x,hole_y=i,j
        elif(board[i][j]=="R"):
            red_x,red_y=i,j
        elif(board[i][j]=="B"):
            blue_x,blue_y=i,j

dequee.append((red_x,red_y,blue_x,blue_y,0))
visited.add((red_x,red_y,blue_x,blue_y))

def move(x,y,di_x,di_y):
    cost=0
    h_check=False

    while(board[x][y]!="#"):
        cost+=1
        x+=di_x
        y+=di_y
        if(x==hole_x and y==hole_y):
            h_check=True
    x-=di_x
    y-=di_y

    return (x,y,cost,h_check)

while(dequee):
    r_x,r_y,b_x,b_y,cost=dequee.popleft()

    if(cost>=10):
        continue

    for i in range(4):
        n_r_x,n_r_y,r_cost,r_check = move(r_x,r_y,dx[i],dy[i])
        n_b_x,n_b_y,b_cost,b_check = move(b_x,b_y,dx[i],dy[i])

        if(not b_check and r_check):
            print(1)
            sys.exit(0)
        elif(not b_check and not r_check):
            if(n_r_x==n_b_x and n_r_y==n_b_y):
                if(r_cost>b_cost):
                    n_r_x-=dx[i]
                    n_r_y-=dy[i]
                else:
                    n_b_x-=dx[i]
                    n_b_y-=dy[i]
            
            if((n_r_x,n_r_y,n_b_x,n_b_y) not in visited):
                visited.add((n_r_x,n_r_y,n_b_x,n_b_y))
                dequee.append((n_r_x,n_r_y,n_b_x,n_b_y,cost+1))

print(0)