import sys

n=int(sys.stdin.readline().rstrip())
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
dp=[[float('-inf'),float('-inf')] for i in range(n)]
dp[0][0]=array[0]

for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+array[i],array[i])
    dp[i][1]=max(dp[i-1][1]+array[i],dp[i-1][0])

print(max(map(max, dp)))