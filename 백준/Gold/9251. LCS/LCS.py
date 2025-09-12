import sys

A=list(sys.stdin.readline().rstrip())
B=list(sys.stdin.readline().rstrip())

dp=[0 for i in range(len(A)+1)]
dp_1=[0 for i in range(len(A)+1)] # 건드리는 배열 기준

max_value=float('-inf')

for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        if (B[i-1]==A[j-1]):
            dp_1[j]=dp[j-1]+1
        else:
            dp_1[j]=max(dp[j],dp_1[j-1])

    max_value=max(dp_1)

    dp=dp_1[:]
    dp_1=[0 for i in range(len(A)+1)]

print(max_value)
