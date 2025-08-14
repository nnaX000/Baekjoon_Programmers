import sys
import math

N=int(sys.stdin.readline().rstrip())

dp=[float('inf') for i in range(N+1)]

dp[1]=1

if(math.sqrt(N).is_integer()):
    print(1)
else:
    for i in range(2,N+1):
        if(math.sqrt(i).is_integer()):
            dp[i]=1
        else:
            for j in range(1,int(math.sqrt(i)+1)):
                dp[i]=min(dp[i],dp[i-(j*j)]+1)
    print(dp[N])