import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    n=int(sys.stdin.readline().rstrip())
    dp=[0 for j in range(n+1)]

    if(n>=1):
        dp[1]=1

    if(n>=2):
        dp[2]=1

    if(n>=3):
        dp[3]=1
        
    for j in range(2,n+1):
        if(j-3>=1):
            dp[j]+=dp[j-3]
        if(j-2>=1):
            dp[j]+=dp[j-2]
        if(j-1>=1):
            dp[j]+=dp[j-1]

    print(dp[-1])