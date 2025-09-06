import sys

N=int(sys.stdin.readline().rstrip())

A=[float('inf')]
A.extend(list(map(int,sys.stdin.readline().rstrip().split(' '))))

dp=[float('inf') for i in range(N+1)]
dp[1]=0

for i in range(1,N):
    tmp=A[i]
    for j in range(i+1,i+tmp+1):
        if(j<N+1):
            dp[j]=min(dp[i]+1,dp[j])

if(dp[N]==float('inf')):
    print(-1)
else:
    print(dp[N])