import sys

n=int(sys.stdin.readline().rstrip())
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp=[0 for i in range(n)]

dp[0]=array[0]

for i in range(1,n):
    dp[i]=max(dp[i-1]+array[i],array[i])

print(max(dp))