def solution(n, results):
    answer = 0
    dp=[[False for i in range(n+1)] for j in range(n+1)]
    
    for a,b in results:
        dp[a][b] = True
        
    for i in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                dp[a][b] = dp[a][b] or (dp[a][i] and dp[i][b])
                
    for i in range(1,n+1):
        total=0
        for j in range(1,n+1):
            if(dp[i][j]):
                total+=1
                
        for j in range(1,n+1):
            if(dp[j][i]):
                total+=1
        
        if(total==n-1):
            answer+=1
            
    return answer