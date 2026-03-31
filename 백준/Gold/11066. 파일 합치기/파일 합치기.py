import sys

input=sys.stdin.readline

T=int(input())

for i in range(T):
    K=int(input())
    arr=list(map(int,input().split()))
    prefix=[0]
    dp=[[0]*K for _ in range(K)]

    for j in range(len(arr)):
        prefix.append(prefix[j]+arr[j])

    for j in range(2,K+1):
        for l in range(K-j+1):
            end=l+j-1
            dp[l][end]=float('inf')

            total=prefix[end+1]-prefix[l]

            for k in range(l,end):
                dp[l][end]=min(dp[l][end],dp[l][k]+dp[k+1][end]+total)

    print(dp[0][K-1])