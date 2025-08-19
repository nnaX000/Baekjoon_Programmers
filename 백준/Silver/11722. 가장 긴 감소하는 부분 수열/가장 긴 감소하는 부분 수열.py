import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp=[1 for i in range(N)]

for i in range(1,N):
    for j in range(0,i):
        if(A[i]<A[j]):
            dp[i]=max(dp[i],1+dp[j])

print(max(dp))