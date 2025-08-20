import sys

N=int(sys.stdin.readline().rstrip())

dp=[0 for i in range(31)]
dp[0]=1
dp[2]=3
dp[4]=11
tmp=11

for i in range(5,N+1):
    if(i%2==1):
        dp[i]=0
    else:
        tmp-=dp[i-4]*3
        tmp+=dp[i-4]*2
        tmp+=dp[i-2]*3
        dp[i]=tmp

print(dp[N])