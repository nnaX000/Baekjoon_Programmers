def solution(info, edges):
    graph = [[] for i in range(len(info))]
    max_value = float('-inf')
    sheep = 0
    wolf = 0
    
    for a,b in edges:
        graph[a].append(b)
        
    visited=set()
    visited.add(0)
    
    if(info[0]==0):
        sheep+=1
    else:
        wolf+=1
    
    def dfs(visited,sheep,wolf):
        nonlocal max_value
        
        if(sheep<=wolf):
            return
        else:
            max_value = max(max_value,sheep)
        
        for i in range(len(graph)):
            if(i in visited):
                for j in range(len(graph[i])):
                    if(graph[i][j] not in visited):
                        visited.add(graph[i][j])
                        
                        if(info[graph[i][j]]==0):
                            sheep+=1
                        else:
                            wolf+=1

                        dfs(visited,sheep,wolf)

                        if(info[graph[i][j]]==0):
                            sheep-=1
                        else:
                            wolf-=1
                            
                        visited.remove(graph[i][j])
    
    dfs(visited,sheep,wolf)
    
    return max_value