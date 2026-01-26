import sys

input=sys.stdin.readline

N,M,x,y,K=map(int,input().split())
answer=[]

# 가장 처음 주사위는 모든면에 0
# 주사위를 굴렸을 때 이동한 칸에 쓰여있는 수가 0이면 주사위 바닥면에 쓰여 있는 수가 칸에 복사
# 0이 아닌 경우 칸에 쓰여있는 수가 주사위 바닥면에 복사, 칸은 0이 된다.

across={
    1:6,
    6:1,
    3:4,
    4:3,
    2:5,
    5:2
}

direction={
    1: [3,4,2,5],
    2: [3,4,6,1],
    3: [6,1,2,5],
    4: [1,6,2,5],
    5: [3,4,1,6],
    6: [3,4,5,2]
}

dx=[0,0,-1,1]
dy=[1,-1,0,0]

space=[list(map(int,input().split())) for _ in range(N)]

#동 1, 서 2, 북 3, 남 4

order=list(map(int,input().split()))

dice=[0 for _ in range(7)] # 동 서 남 북 위 아래

for i in order:
    nx=x+dx[i-1]
    ny=y+dy[i-1]

    if(0<=nx<N and 0<=ny<M):
        x=nx
        y=ny
        
        if(i==1):
            dice[1],dice[5],dice[2],dice[6]=dice[6],dice[1],dice[5],dice[2]
        elif(i==2):
            dice[2],dice[6],dice[1],dice[5]=dice[6],dice[1],dice[5],dice[2]
        elif(i==3):
            dice[4],dice[5],dice[3],dice[6]=dice[6],dice[4],dice[5],dice[3]
        else:
            dice[3],dice[5],dice[4],dice[6]=dice[6],dice[3],dice[5],dice[4]

        if(space[nx][ny]==0):
            space[nx][ny]=dice[6]
        else:
            dice[6]=space[nx][ny]
            space[nx][ny]=0

        answer.append(dice[5])

for i in answer:
    print(i)