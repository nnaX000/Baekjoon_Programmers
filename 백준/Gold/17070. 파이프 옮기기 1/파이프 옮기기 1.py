import sys

input=sys.stdin.readline

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지, 방향 가로
# 파이프는 항상 빈 칸만 차지해야 한다.
# 빈 칸이 0, 벽이 1

N=int(input())
house=[list(map(int,input().split())) for _ in range(N)]
dp=[[[0,0,0] for _ in range(N)] for _ in range(N)] # 해당 칸에 가로, 세로, 대각선으로 오는 경우

dp[0][1][0]=1

for i in range(N):
    for j in range(2 if i==0 else 0,N):
        #가로
        if(j-1>=0 and house[i][j]==0):
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]

        #세로
        if(i-1>=0 and house[i][j]==0):
            dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]

        #대각선
        if(i-1>=0 and j-1>=0 and house[i][j]==0 and house[i-1][j]==0 and house[i][j-1]==0):
            dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[-1][-1]))