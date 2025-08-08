import sys

def dfs(visited,tmp):
    if(len(tmp)==N):
        print(*tmp)
    for i in range(len(nums)):
        if(not visited[i]):
            tmp.append(nums[i])
            visited[i]=True
            dfs(visited,tmp)
            tmp.pop()
            visited[i]=False

N=int(sys.stdin.readline().rstrip())

visited=[False for i in range(N)]
tmp=[]
nums=[i+1 for i in range(N)]

dfs(visited,tmp)