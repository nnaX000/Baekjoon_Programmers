import sys

input=sys.stdin.readline

N,M=map(int,input().split()) #유저 수, 친구 관계 수
dp=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]
mv=float('inf')
mv_p=0

for i in range(1,N+1):
    dp[i][i]=0

for i in range(M):
    a,b=map(int,input().split())

    dp[a][b]=1
    dp[b][a]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

for i in range(1,N+1):
    tmp=0
    for j in range(1,N+1):
        tmp+=dp[i][j]

    if(tmp<mv):
        mv=tmp
        mv_p=i

print(mv_p)