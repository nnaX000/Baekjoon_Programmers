#[첫번째인경우,두번째인경우,max] [50,0,0] [20,70,50]
# [95,65,70] [150,
num=int(input())
array=[0,0]
for i in range(num):
    temp=int(input())
    array.append(temp)
array.append(0)
array.append(0)
dp=[[0,0,0] for i in range(num+4)]
dp[2][0]=array[2]
dp[2][2]=array[2]
for i in range(3,num+2):
    dp[i][0]=dp[i-2][2]+array[i]
    dp[i][1]=dp[i-1][0]+array[i]
    dp[i][2]=max(dp[i][0],dp[i][1])
print(max(dp[num+1]))