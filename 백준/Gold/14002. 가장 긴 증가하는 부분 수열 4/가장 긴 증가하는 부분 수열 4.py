import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp=[1 for i in range(N)]
dp_num=[]

max_idx=0

for i in range(N):
    dp_num.append([A[i]])

for i in range(N):
    for j in range(i,-1,-1):
        if(A[i]>A[j]):
            if(dp[i]<dp[j]+1):
                dp[i]=dp[j]+1
                dp_num[i]=dp_num[j]+[A[i]]

    if(dp[i]>dp[max_idx]):
        max_idx=i

print(dp[max_idx])
print(*dp_num[max_idx])