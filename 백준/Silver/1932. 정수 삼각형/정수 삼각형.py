num=int(input())
dp=[]
array=[]
for i in range(num):
    temp=list(map(int,input().split(' ')))
    array.append(temp)
dp=array.copy()
for i in range(1,len(array)):
    for j in range(len(array[i])):
        if(j==0):
            dp[i][j]=dp[i-1][0]+dp[i][j]
        elif(j==len(array[i])-1):
            dp[i][j] = dp[i-1][len(array[i])-2]+dp[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1]+dp[i][j],dp[i-1][j]+dp[i][j])
print(max(dp[-1]))