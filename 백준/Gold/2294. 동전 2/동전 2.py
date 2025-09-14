import sys

n,k=map(int,sys.stdin.readline().rstrip().split(' '))
coin=set([int(sys.stdin.readline().rstrip()) for i in range(n)])
dp=[float('inf') for i in range(k+1)]
dp[0]=0

for i in range(1,k+1):
    for j in coin:
        if(i>=j):
            dp[i]=min(dp[i],dp[i-j]+1)

if(dp[k]==float('inf')):
    print(-1)
else:
    print(dp[k])