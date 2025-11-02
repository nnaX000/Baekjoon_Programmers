import sys
sys.setrecursionlimit(3000)

def solution(n, m, x, y, r, c, k):
    answer = ''
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    direction = ["d","l","r","u"]
    #x,y 출발위치 / r,c 탈출위치 / k 탈출까지 이동해야 하는 거리
    
    def dfs(x,y,dist,path):
        nonlocal answer
        
        if(answer!=''):
            return
        
        remain = abs(r - x - 1) + abs(c - y - 1)
        # 남은 거리로 도달 불가능한 경우 가지치기
        if remain > k - dist or (remain % 2 != (k - dist) % 2):
            return
        
        if(x == r-1 and y == c-1 and dist==k):
            answer = path
            return
        
        for i in range(4):
            if(0<=x+dx[i]<n and 0<=y+dy[i]<m):
                dfs(x+dx[i],y+dy[i],dist+1,path+direction[i])
                
    dfs(x-1,y-1,0,"")
                
    return answer if answer!="" else "impossible"