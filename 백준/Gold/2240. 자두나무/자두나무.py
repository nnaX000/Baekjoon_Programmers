import sys

input=sys.stdin.readline

T,W=map(int,input().split())

# x축 : 움직인 횟수
# y축 : idx
# dp[x][y] = 자두가 자두를 먹은 최대 개수

dp=[[0 for _ in range(T)] for _ in range(W+1)]

for i in range(T):
    jadu=int(input())

    if(i==0):
        if(jadu==1):
            dp[0][0]=1
        else:
            dp[1][0]=1
    else:

        for j in range(0,W+1):
            dp[j][i] = dp[j][i-1]

            if(j%2==0): # 나무 1에 있는 경우
                if(jadu==1):
                    dp[j][i]=max(dp[j][i],dp[j][i-1]+1)
                else:
                    if(j-1>=0):
                        dp[j][i]=max(dp[j][i],dp[j-1][i-1]+1)

            else: # 나무 2에 있는 경우
                if(jadu==1):
                    dp[j][i]=max(dp[j][i],dp[j-1][i-1]+1)
                else:
                    if(j-1>=0):
                        dp[j][i]=max(dp[j][i],dp[j][i-1]+1)


print(max(max(i) for i in dp))