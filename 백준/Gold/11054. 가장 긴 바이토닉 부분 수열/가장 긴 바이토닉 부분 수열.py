N=int(input())

array=list(map(int,input().split(' ')))

big_dp=[1]*N
small_dp=[1]*N
max_answer=0

for j in range(0,N):
        for k in range(j):
            if(array[j]>array[k]):
                big_dp[j]=max(big_dp[k]+1,big_dp[j])

for j in range(N-1,-1,-1):
        for k in range(N-1,j,-1):
            if(array[j]>array[k]):
                small_dp[j]=max(small_dp[k]+1,small_dp[j])

for i in range(N):
     if(small_dp[i]+big_dp[i]-1>max_answer):
          max_answer=small_dp[i]+big_dp[i]-1

print(max_answer)
