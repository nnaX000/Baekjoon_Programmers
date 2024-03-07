#[빨,초,파]
num=int(input())
array=[]
for i in range(num):
    temp=list(map(int,input().split(' ')))
    array.append(temp)
dp=[[0,0,0] for i in range(num)]
dp[0]=array[0]
for i in range(1,num):
    dp[i][0]=min(dp[i-1][1]+array[i][0],array[i][0]+dp[i-1][2])
    dp[i][1]=min(dp[i-1][0]+array[i][1],array[i][1]+dp[i-1][2])
    dp[i][2] = min(dp[i - 1][0] + array[i][2], array[i][2] + dp[i - 1][1])
print(min(dp[-1]))