import sys

input=sys.stdin.readline

N=int(input())
house=[list(map(int,input().split())) for _ in range(N)]

dp=[[[0,0,0] for _ in range(N)] for _ in range(N)] # 가로, 세로, 대각선
dp[0][1][0]=1

for i in range(N):
    for j in range(1 if i==0 else 0,N):
        if(house[i][j]==0):
            #해당 칸에 가로로 오는 경우
            if(0<=j-1<N and house[i][j-1]==0):
                dp[i][j][0]+=dp[i][j-1][0]
                dp[i][j][0]+=dp[i][j-1][2]

            #해당 칸에 세로로 오는 경우
            if(0<=i-1<N and house[i-1][j]==0):
                dp[i][j][1]+=dp[i-1][j][1]
                dp[i][j][1]+=dp[i-1][j][2]

            #해당 칸에 대각선으로 오는 경우
            if(0<=i-1<N and 0<=j-1<N and house[i-1][j-1]==0 and house[i-1][j]==0 and house[i][j-1]==0):
                dp[i][j][2]+=dp[i-1][j-1][0]
                dp[i][j][2]+=dp[i-1][j-1][1]
                dp[i][j][2]+=dp[i-1][j-1][2]
                
print(sum(dp[-1][-1]))