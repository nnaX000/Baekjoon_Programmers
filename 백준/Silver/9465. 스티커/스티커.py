import sys

input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())

    stiker=[list((map(int,input().rstrip().split()))) for _ in range(2)]

    dp=[[0 for i in range(n)] for _ in range(2)]
    dp[0][0]=stiker[0][0]
    dp[1][0]=stiker[1][0]

    for j in range(1,n):
        if(j==1):
            dp[1][j]=dp[0][0]+stiker[1][j]
            dp[0][j]=dp[1][0]+stiker[0][j]
        else:
            dp[0][j]=max(dp[1][j-1]+stiker[0][j],max(dp[0][j-2],dp[1][j-2])+stiker[0][j])
            dp[1][j]=max(dp[0][j-1]+stiker[1][j],max(dp[0][j-2],dp[1][j-2])+stiker[1][j])

    print(max(max(i) for i in dp))