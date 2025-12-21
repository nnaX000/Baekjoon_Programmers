import sys

input=sys.stdin.readline

N=int(input().rstrip())

stair=[]

for i in range(N):
    stair.append(int(input().rstrip()))

stair.reverse()
dp=[[0,0] for i in range(len(stair))]
dp[0][0]=stair[0]
max_value=float('-inf')

for i in range(1,len(dp)):
    if(i==1):
        dp[i][1]=dp[i-1][0]+stair[i]
    elif(i==2):
        dp[i][0]=max(dp[i-2])+stair[i]
    else:
        dp[i][0]=max(dp[i-2])+stair[i]
        dp[i][1]=dp[i-1][0]+stair[i]

for i in range(len(dp)):
    for j in range(2):
        max_value=max(max_value,dp[i][j])

print(max_value)