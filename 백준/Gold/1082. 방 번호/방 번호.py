import sys
from collections import defaultdict

N=int(sys.stdin.readline().rstrip())
P=list(map(int,sys.stdin.readline().rstrip().split(' ')))
M=int(sys.stdin.readline().rstrip())

dp=[["none"] for i in range(M+1)]

max_value=float('-inf')

for i in range(len(P)):
    if(P[i]<=M):
        dp[P[i]]=[str(i)]

for i in range(1,M+1):
    for j in range(0,i):
        if(dp[j][0]!="none" and dp[i-j][0]!="none"):
            tmp=dp[j]+dp[i-j]
            origin=0

            if(dp[i][0]!="none"):
                origin=int(''.join(sorted(dp[i],reverse=True))) 

            if(origin<int(''.join(sorted(tmp,reverse=True)))):
                dp[i]=tmp

for i in dp:
    if(i[0]!="none"):
        tmp=int(''.join(sorted(i,reverse=True)))
        max_value=max(max_value,tmp)

print(max_value)