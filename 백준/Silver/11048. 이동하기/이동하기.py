import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
miro=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(N)]
dp=[i[:] for i in miro]

for i in range(N):
    for j in range(M):
        origin=dp[i][j]

        if(0<=i-1<N):
            dp[i][j]=max(dp[i][j],dp[i-1][j]+origin)
        
        if(0<=j-1<M):
            dp[i][j]=max(dp[i][j],dp[i][j-1]+origin)

        if(0<=i-1<N and 0<=j-1<M):
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+origin)

print(dp[N-1][M-1])