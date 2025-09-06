import sys

N=int(sys.stdin.readline().rstrip())
board=list(map(int,sys.stdin.readline().rstrip().split(' ')))
M=int(sys.stdin.readline().rstrip())
question=[]
for i in range(M):
    question.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
dp=[[False for i in range(N+1)] for j in range(N+1)]

for i in range(N,0,-1):
    for j in range(N,0,-1):
        if(i>j):
            continue

        if(i==j):
            dp[i][j]=True
            continue

        if(j-i==1):
            if(board[i-1]==board[j-1]):
                dp[i][j]=True
            continue

        if(board[i-1]==board[j-1] and dp[i+1][j-1]):
            dp[i][j]=True

for i in question:
    x,y=i[0],i[1]
    if dp[x][y]:
        print(1)
    else:
        print(0) 