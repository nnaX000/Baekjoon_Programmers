def dfs(visited,exception,wires,last_node):
    cnt = 1

    for i in range(len(wires)):
        if(last_node == wires[i][0] and i!=exception and not visited[i]):
            visited[i] = True
            cnt += dfs(visited,exception,wires,wires[i][1])
            visited[i] = False
        elif(last_node == wires[i][1] and i!=exception and not visited[i]):
            visited[i] = True
            cnt += dfs(visited,exception,wires,wires[i][0])
            visited[i] = False
            
    return cnt

def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        visited=[False for i in range(len(wires))]
        count = 0
        last_node = 0
        
        for j in range(1,n+1):
            if(j not in wires[i]):
                last_node = j
                break
                
        count = dfs(visited,i,wires,last_node) # visited, 제외할 인덱스, 간선 정보, last node
        count_2 = n-count
        answer = min(answer,abs(count-count_2))
        
    return answer