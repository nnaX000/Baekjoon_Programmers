import sys

input=sys.stdin.readline

n=int(input())

dp=[float('inf') for i in range(n+1)]
dp[0]=0

for i in range(n+1):
    idx=1
    while(idx*idx<=i):
        dp[i]=min(dp[i],dp[i-(idx*idx)]+1)
        idx+=1

print(dp[-1])