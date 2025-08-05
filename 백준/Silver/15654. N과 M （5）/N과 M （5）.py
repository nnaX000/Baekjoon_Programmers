import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
array.sort()

def dfs(visited,array,tmp):
    if(len(tmp)==M):
        for j in tmp:
            print(j,end=" ")
        print()
        return
    
    for i in range(len(array)):
        if(not visited[i]):
            tmp.append(array[i])
            visited[i]=True
            dfs(visited,array,tmp)
            visited[i]=False
            tmp.pop()

visited=[False for i in range(len(array))]
tmp=[]
dfs(visited,array,tmp)