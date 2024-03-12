def check(m,n,puddles):
    value=True
    for i in puddles:
        tmp=i
        if(tmp[0]-1==n and tmp[1]-1==m):
           value=False
           break
    return value


def solution(m, n, puddles):
    dp=[[0]*m for i in range(n)]
    for i in range(1,m):
        if(check(0,i,puddles)):
            dp[0][i]=1
        else:break
    for i in range(1,n):
        if(check(i,0,puddles)):
            dp[i][0]=1
        else:
            break
    for i in range(1,m):
        for j in range(1,n):
            if(check(j,i,puddles)):
                dp[j][i]=dp[j][i-1]+dp[j-1][i]
            else:
                dp[j][i] = 0
    print(dp)
    answer = dp[n-1][m-1]
    return answer%1000000007