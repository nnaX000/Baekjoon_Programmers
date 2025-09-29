def dfs(current,visited,count,dungeons):
    max_count = count
    for i in range(len(visited)):
        if(current>=dungeons[i][0] and not visited[i]):
            current-=dungeons[i][1]
            visited[i]=True
            result = dfs(current,visited,count+1,dungeons)
            max_count = max(max_count,result)
            current+=dungeons[i][1]
            visited[i]=False
    return max_count

def solution(k, dungeons):
    visited = [False for i in range(len(dungeons))]
    max_value = dfs(k,visited,0,dungeons)
    return max_value