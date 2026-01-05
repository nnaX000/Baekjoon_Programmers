import sys

input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())

    stiker=[list((map(int,input().rstrip().split()))) for _ in range(2)]
    n_stiker=[]

    for j in range(n):
        n_stiker.append([stiker[0][j],stiker[1][j]])

    dp=[[0,0] for _ in range(n)]
    dp[0][0]=n_stiker[0][0]
    dp[0][1]=n_stiker[0][1]

    for j in range(1,n):
        if(j==1):
            dp[j][1]=dp[0][0]+n_stiker[j][1]
            dp[j][0]=dp[0][1]+n_stiker[j][0]
        else:
            dp[j][0]=max(dp[j-1][1]+n_stiker[j][0],max(dp[j-2])+n_stiker[j][0])
            dp[j][1]=max(dp[j-1][0]+n_stiker[j][1],max(dp[j-2])+n_stiker[j][1])

    print(max(max(i) for i in dp))