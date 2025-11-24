import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

dp_num=[1 for i in range(N)]
dp=[]

for i in A:
    dp.append([i])

for i in range(1,len(A)):
    for j in range(i):
        if(A[j]<A[i]):
            if(dp_num[i]<dp_num[j]+1):
                dp_num[i]=dp_num[j]+1
                tmp=dp[j][:]
                tmp.append(A[i])
                dp[i]=tmp

max_value=max(dp_num)

for i in range(len(dp)):
    if(len(dp[i])==max_value):
        print(max_value)
        print(*dp[i])
        break