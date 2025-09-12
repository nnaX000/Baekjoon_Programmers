import sys

N=int(sys.stdin.readline().rstrip())
dp=[0 for i in range(100)] # [최대 가질 수 있는 개수, 클립보드 개수]

dp[0]=1
dp[1]=2
dp[2]=3
dp[3]=4
dp[4]=5
dp[5]=6

for i in range(6,N):
    dp[i]=max(dp[i-1]+1,dp[i-2]+2)
    for j in range(3,i+1):
        dp[i]=max(dp[i],dp[i-j]*(j-1))

print(dp[N-1])