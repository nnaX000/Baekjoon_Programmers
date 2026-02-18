import sys

input=sys.stdin.readline

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
dp=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(graph[i][j]==1):
            dp[i][j]=1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(dp[j][k]==0 and dp[j][i]==1 and dp[i][k]==1):
                dp[j][k]=1

for i in range(N):
    print(*dp[i])