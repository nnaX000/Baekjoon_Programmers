import sys

input=sys.stdin.readline

n=int(input())
dp=[[0 for _ in range(n)] for _ in range(n+1)]

for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)):
        dp[i][j]=tmp[j]

for i in range(1,n+1):
    for j in range(i):
        if(j==0):
            dp[i][j]+=dp[i-1][j]
        elif(j==i-1):
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[-1]))