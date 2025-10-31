def solution(info, n, m):
    answer = 0
    a_min = float('inf')
    item_num = len(info)
    dp = [[float('inf') for i in range(m)] for j in range(item_num+1)]
    
    #A가 훔치는 경우
    if info[0][0] < n:
        dp[0][0] = info[0][0]
    
    #B가 훔치는 경우
    if info[0][1] < m: 
        dp[0][info[0][1]] = 0
    
    for i in range(1,item_num):
        for j in range(m): #B 흔적
            if(dp[i-1][j] == float('inf')):
                continue
            
            #A가 훔치는 경우
            dp[i][j] = min(dp[i][j],dp[i-1][j]+info[i][0])
            
            #B가 훔치는 경우
            if(j+info[i][1]<m):
                dp[i][j + info[i][1]] = min(dp[i][j + info[i][1]], dp[i-1][j])
                
    for i in range(m):
        if(dp[item_num-1][i]<n):
            a_min = min(a_min,dp[item_num-1][i])
            
    return a_min if a_min != float('inf') else -1