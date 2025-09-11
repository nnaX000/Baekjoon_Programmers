import sys

A=list(sys.stdin.readline().rstrip())
B=list(sys.stdin.readline().rstrip())

dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
max_value=float('-inf')

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if(A[i-1]==B[j-1]):
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=0

        if(max_value<dp[i][j]):
            max_value=dp[i][j]

print(max_value)