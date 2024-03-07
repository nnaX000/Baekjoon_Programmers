#[0인 경우,9인 경우,그 외 숫자인 경우,합계]
num=int(input())
dp=[[0,0,0,0,0,0,0,0,0,0] for i in range(101)]
dp[0]=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,num+1):
    for j in range(10):
        if(j==0):
            dp[i][j]=dp[i-1][j+1]
        elif(j==9):
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[num-1])%1000000000)