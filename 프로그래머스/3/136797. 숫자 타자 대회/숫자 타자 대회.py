import sys
from functools import lru_cache
sys.setrecursionlimit(300000)

def solution(numbers):
    answer = float('inf')
    dist = [[float('inf') for i in range(10)] for j in range(10)]
    
    for i in range(10):
        dist[i][i] = 1
        
    for i,j in [(1,2),(1,4),(2,1),(2,5),(2,3),(3,2),(3,6),(4,1),(4,5),(4,7),(5,2),(5,4),(5,6),(5,8),(6,3),(6,5),(6,9),(7,4),(7,8),(8,7),(8,5),(8,9),(8,0),(9,8),(9,6),(0,8)]:
        dist[i][j] = 2
        
    for i,j in [(1,5),(2,4),(2,6),(3,5),(4,2),(4,8),(5,1),(5,3),(5,7),(5,9),(6,2),(6,8),(7,5),(7,0),(8,4),(8,6),(9,5),(9,0),(0,7),(0,9)]:
        dist[i][j] = 3
        
    for i in range(10):
        for j in range(10):
            for k in range(10):
                dist[j][k] = min(dist[j][k],dist[j][i]+dist[i][k])
                
    @lru_cache(maxsize=None)            
    def dfs(left, right, current):
        nonlocal answer
        
        if(current==len(numbers)):
            return 0
        
        target = int(numbers[current])
        
        if(target == left):
            return dfs(left,right,current+1)+1
        elif(target == right):
            return dfs(left,right,current+1)+1
        else:
            #왼손 옮겨서 치는 경우
            left_result = dfs(target,right,current+1)+dist[left][target]

            #오른손으로 옮겨서 치는 경우
            right_result = dfs(left,target,current+1)+dist[right][target]
            
        return min(left_result,right_result)
        
    return dfs(4,6,0)