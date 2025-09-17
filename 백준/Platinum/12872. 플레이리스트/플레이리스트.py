import sys

N, M, P = map(int,sys.stdin.readline().rstrip().split(' '))

dp=[[0 for i in range(N+1)] for j in range(P+1)]
dp[0][0] = 1

for i in range(1,P+1):
    for j in range(1,N+1):
        dp[i][j]=(dp[i-1][j-1]*(N-j+1))+(dp[i-1][j]*max(j-M,0))

print(dp[P][N]%1000000007)