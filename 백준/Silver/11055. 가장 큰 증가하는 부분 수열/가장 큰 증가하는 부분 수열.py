import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp=[[i] for i in A]
max_value=0

dp[0]=[A[0]]

for i in range(N):
    for j in range(0,i):
        if(A[i]>A[j]):
            tmp=sum(dp[j])+A[i]
            if(tmp>sum(dp[i])):
                dp[i]=dp[j]+[A[i]]
    
    if(sum(dp[i])>max_value):
        max_value=sum(dp[i])
        
print(max_value)