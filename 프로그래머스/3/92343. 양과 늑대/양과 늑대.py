import sys

def solution(info, edges):
    # 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다. 
    # 0이 양, 1이 늑대
    
    answer=float('-inf')
    
    sys.setrecursionlimit(10**6)
    
    ways=[[] for _ in range(len(info)+1)]
    parents=[0 for _ in range(len(info)+1)]
    visited=[0 for _ in range(len(info)+1)]
    
    for a,b in edges:
        ways[a].append(b)
        parents[b]=a
        
    parents[0]=-1
        
    def dfs(avail,s_n,w_n):
        nonlocal answer
        
        if(s_n<=w_n):
            return
        
        answer=max(answer,s_n)
            
        for idx,i in enumerate(avail):
            tmp=avail[:idx]+avail[idx+1:]+ways[i]
            
            if(info[i]==1):
                dfs(tmp,s_n,w_n+1)
            else:
                dfs(tmp,s_n+1,w_n)
    
    dfs(ways[0],1,0)
        
    return answer