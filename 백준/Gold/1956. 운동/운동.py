import sys

input=sys.stdin.readline

V,E=map(int,input().split())

# 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

edges=[[] for _ in range(V+1)]

dp=[[float('inf') for _ in range(V+1)] for _ in range(V+1)]

answer=float('inf')

for i in range(E):
    a,b,c=map(int,input().split())
    dp[a][b]=c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            dp[i][j]=min(dp[i][k]+dp[k][j],dp[i][j])

for i in range(1,V+1):
    answer=min(answer,dp[i][i])

print(answer if answer!=float('inf') else -1)  