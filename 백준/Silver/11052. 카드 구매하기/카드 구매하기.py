import sys
import copy

N=int(sys.stdin.readline().rstrip())
cards=[0]
cards.extend(list(map(int,sys.stdin.readline().rstrip().split(' '))))

dp=copy.deepcopy(cards)

for i in range(1,N+1):
    for j in range((i//2)+1):
        dp[i]=max(dp[i],dp[j]+dp[i-j])
    
print(dp[N])