import sys

input=sys.stdin.readline

n=int(input())

tri=[]

for i in range(n):
    tri.append(list(map(int,input().split())))

dp=[]

for i in range(1,n+1):
    dp.append([float('-inf')]*i)

dp[0][0]=tri[0][0]

for i in range(1,n):
    for j in range(len(dp[i])):
        if(j==0):
            dp[i][j]=dp[i-1][0]+tri[i][j]
        elif(j==len(dp[i])-1):
            dp[i][j]=dp[i-1][-1]+tri[i][j]
        else:
            dp[i][j]=max(dp[i-1][j]+tri[i][j],dp[i-1][j-1]+tri[i][j])

print(max(dp[-1]))