N=int(input())

dp=[1]*10

for i in range(1,N):
    for j in range(len(dp)):
        dp[j]=sum(dp[j:10])
        
print(sum(dp)%10007)