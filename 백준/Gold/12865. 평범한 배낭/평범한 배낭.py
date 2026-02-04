import sys

input=sys.stdin.readline

N,K=map(int,input().split())

dp=[0 for _ in range(K+1)]

for i in range(N):
    W,V=map(int,input().split()) # 무게, 가치


    for j in range(K,W-1,-1):
        dp[j]=max(dp[j],dp[j-W]+V)

print(max(dp))