import sys

T=int(sys.stdin.readline().rstrip())
array=[int(sys.stdin.readline().rstrip()) for i in range(T)]

dp = [1 for i in range(max(array)+1)]

for i in range(2,max(array)+1):
    dp[i]+=dp[i-2]

for i in range(3,max(array)+1):
    dp[i]+=dp[i-3]

for i in array:
    print(dp[i])