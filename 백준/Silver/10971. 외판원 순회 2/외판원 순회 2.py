import sys

N=int(sys.stdin.readline().rstrip())
expense=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(N)]

min_value=100000001

def dfs(visited,tmp,cost):
    global min_value

    if(len(tmp)==N):
        if(expense[tmp[-1]][tmp[0]]==0):
            return
        else:
            cost+=expense[tmp[-1]][tmp[0]]
            if(cost<min_value):
                min_value=cost
            return

    for i in range(N):
        if(not visited[i]):
            if(not tmp):
                visited[i]=True
                tmp.append(i)
                dfs(visited,tmp,cost)
                tmp.pop()
                visited[i]=False
            elif(expense[tmp[-1]][i]!=0):
                visited[i]=True
                cost+=expense[tmp[-1]][i]
                tmp.append(i)
                dfs(visited,tmp,cost)
                tmp.pop()
                cost-=expense[tmp[-1]][i]
                visited[i]=False

visited=[False for i in range(N)]
tmp=[]

dfs(visited,tmp,0)
print(min_value)