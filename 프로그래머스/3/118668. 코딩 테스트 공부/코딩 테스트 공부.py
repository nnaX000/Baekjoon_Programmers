#[문제 푸는 데 필요한 알고력, 문제 푸는 데 필요한 코딩력, 문제 풀었을 때 증가하는 알고력, 문풀증 코딩, cost]
def solution(alp, cop, problems):
    
    max_alg = max(i[0] for i in problems)
    max_cod = max(i[1] for i in problems)
    
    # alp, cop이 이미 목표보다 클 수도 있으니 조정
    alp = min(alp, max_alg)
    cop = min(cop, max_cod)

    # dp[i][j] = i알고력, j코딩력에 도달하는 최소 시간
    dp = [[float('inf')] * (max_cod + 2) for _ in range(max_alg + 2)]
    dp[alp][cop] = 0
    
    for i in range(alp,max_alg+1):
        for j in range(cop,max_cod+1):
            dp[i+1][j] = min(dp[i][j]+1,dp[i+1][j])
            dp[i][j+1] = min(dp[i][j]+1,dp[i][j+1])
            
            for na,nc,ia,ic,cost in problems:
                if(i>=na and j>=nc):
                    ni = min(i+ia,max_alg)
                    nj = min(j+ic,max_cod)
                    dp[ni][nj] = min(dp[ni][nj],dp[i][j]+cost)
            
    return dp[max_alg][max_cod]