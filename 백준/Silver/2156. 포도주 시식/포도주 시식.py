num=int(input())
array=[]
for i in range(num):
    temp=int(input())
    array.append(temp)
dp=[[0,0,0] for i in range(num)]
dp[0][0]=array[0]
dp[0][1]=array[0]
dp[0][2]=0

if(num>1):
    dp[1][0]=array[1]
    dp[1][1]=array[0]+array[1]
    dp[1][2]=array[0]

for i in range(2,num):
    chance=array[i]
    dp[i][0]=dp[i-1][2]+array[i]
    dp[i][1]=dp[i-1][0]+array[i]
    dp[i][2]=max(dp[i-1][0],max(dp[i-1][1],dp[i-1][2]))
print(max(dp[-1][0],max(dp[-1][1],dp[-1][2])))