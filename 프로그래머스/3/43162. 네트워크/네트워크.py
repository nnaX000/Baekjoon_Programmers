def solution(n, computers):
    answer=0
    visited=[False]*n
    
    def dfs(node):
        for idx,i in enumerate(node):
            if(not visited[idx] and i==1):
                visited[idx]=True
                dfs(computers[idx])
                
    for i in range(n):
        if(not visited[i]):
            dfs(computers[i])
            answer+=1
        
    return answer