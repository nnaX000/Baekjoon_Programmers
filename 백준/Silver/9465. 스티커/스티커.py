import sys

input=sys.stdin.readline

# 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 
# 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.

T=int(input())

for i in range(T):
    n=int(input())

    stiker=[list(map(int,input().split())) for _ in range(2)]
    dp=[j[:] for j in stiker]

    length=len(stiker[0])

    if(n>=2):
        dp[0][1]+=dp[1][0]
        dp[1][1]+=dp[0][0]

    if(n>=3):
        for j in range(2,length):
            dp[0][j]=max(dp[1][j-2]+dp[0][j],dp[1][j-1]+dp[0][j])
            dp[1][j]=max(dp[0][j-2]+dp[1][j],dp[0][j-1]+dp[1][j])

    print(max(dp[0][-1],dp[1][-1]))