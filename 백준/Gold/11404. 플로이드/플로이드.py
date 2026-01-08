import sys

input=sys.stdin.readline

n=int(input())
m=int(input())

dp=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())

    dp[a][b]=min(c,dp[a][b])

for i in range(1,n+1):
    dp[i][i]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            dp[j][k]=min(dp[j][k],dp[j][i]+dp[i][k])

for i in range(1,len(dp)):
    for j in range(1,n+1):
        if(dp[i][j]!=float('inf')):
            print(dp[i][j],end=" ")
        else:
            print(0,end=" ")
    print()