import sys

N=int(sys.stdin.readline().rstrip())
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))

max_value=0

def dfs(visited,tmp):
    global max_value

    if(len(tmp)==N):
        sum_value=0
        for i in range(N-1):
            sum_value+=abs(tmp[i]-tmp[i+1])
        if(sum_value>max_value):
            max_value=sum_value
        return

    for i in range(len(array)):
        if(not visited[i]):
            tmp.append(array[i])
            visited[i]=True
            dfs(visited,tmp)
            tmp.pop()
            visited[i]=False


visited=[False for i in range(N)]
tmp=[]
dfs(visited,tmp)

print(max_value)