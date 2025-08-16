import sys

T=int(sys.stdin.readline().rstrip())

array=[]

for i in range(T):
    array.append(int(sys.stdin.readline().rstrip()))

max_value=max(array)

dp=[0 for i in range(max_value+1)]

dp[0]=1
dp[1]=1
dp[2]=2

for i in range(3,max_value+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for i in array:
    print(dp[i])