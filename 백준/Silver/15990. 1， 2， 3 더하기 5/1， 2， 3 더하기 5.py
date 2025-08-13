import sys

T=int(sys.stdin.readline().rstrip())
nums=[]

for i in range(T):
    nums.append(int(sys.stdin.readline().rstrip()))

max_value=max(nums)

dp=[[0 for i in range(4)]for j in range(max_value+1)]
dp[1]=[0,1,0,0]
dp[2]=[0,0,1,0]
dp[3]=[0,1,1,1]

for j in range(4,max_value+1):
    dp[j][3]=(dp[j-3][1]+dp[j-3][2])%1000000009
    dp[j][2]=(dp[j-2][1]+dp[j-2][3])%1000000009
    dp[j][1]=(dp[j-1][2]+dp[j-1][3])%1000000009

for i in nums:
    print(sum(dp[i])%1000000009)