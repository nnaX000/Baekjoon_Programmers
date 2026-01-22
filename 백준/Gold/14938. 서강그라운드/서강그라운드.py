import sys

input=sys.stdin.readline

# 낙하산에서 떨어질 때 각 지역에 아이템들이 몇 개 있는지
# 길은 양방향 통행이 가능

n,m,r=map(int,input().split())

items=list(map(int,input().split()))

dp=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for i in range(r):
    a,b,l=map(int,input().split())

    dp[a][b]=l
    dp[b][a]=l

for i in range(1,n+1):
    dp[i][i]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            dp[j][k]=min(dp[j][i]+dp[i][k],dp[j][k])

answer=[0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if(dp[i][j]<=m):
            answer[i]+=items[j-1]

print(max(answer))