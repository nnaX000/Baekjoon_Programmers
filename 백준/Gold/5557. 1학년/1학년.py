import sys

N=int(sys.stdin.readline().rstrip())
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
dp=[[0 for i in range(21)] for j in range(N-1)]
dp[0][array[0]]=1

for i in range(1,N-1):
    for j in range(len(dp[i-1])):
        if(dp[i-1][j]>0):
            if(0<=j+array[i]<=20):
                dp[i][j+array[i]]+=dp[i-1][j]

            if(0<=j-array[i]<=20):
                dp[i][j-array[i]]+=dp[i-1][j]

print(dp[N-2][array[-1]])