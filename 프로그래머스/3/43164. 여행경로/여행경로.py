from collections import deque

def solution(tickets):
    answers = []
    dequee = deque()
    
    tickets.sort()
    visited = [False for i in range(len(tickets))]
    dequee.append((["ICN"],visited)) #path, visited
    
    while(dequee):        
        path, visited = dequee.popleft()
        
        if(all(visited)):
            return path
        
        for i in range(len(tickets)):
            depart = tickets[i][0]
            arrive = tickets[i][1]
            
            if(path[-1]==depart and not visited[i]):
                n_path = path[:]
                n_path.append(arrive)
                n_visited = visited[:]
                n_visited[i] = True
                dequee.append((n_path,n_visited))
