import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
dp=[0 for i in range(M+1)]

for i in range(N):
    V,C,K=map(int,sys.stdin.readline().rstrip().split(' ')) # 무게, 만족도, 개수

    num=1

    while(K>0):
        take=min(K,num)
        weight=V*take
        satis=C*take

        for j in range(M,weight-1,-1):
            dp[j]=max(dp[j],dp[j-weight]+satis)

        K-=take
        num*=2

print(max(dp))