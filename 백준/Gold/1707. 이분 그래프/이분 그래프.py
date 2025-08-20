import sys

sys.setrecursionlimit(10**6)

K=int(sys.stdin.readline().rstrip())

def dfs(color,start):
    global mark

    if(color==1):
        new_color=2
    else:
        new_color=1

    for i in graph[start]:
        if(mark[i]==0):
            mark[i]=new_color
            if not dfs(new_color,i):
                return False
        elif(mark[i]==color):
            return False
    
    return True

for i in range(K):
    V,E=map(int,sys.stdin.readline().rstrip().split(' '))
    check=True
    result=True
    graph=[[] for j in range(V+1)]

    for j in range(E):
        a,b=map(int,sys.stdin.readline().rstrip().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    mark=[0 for k in range(V+1)]

    for j in range(1,V+1):
        if(mark[j]==0):
            mark[j]=1
            result=dfs(1,j)
            if(not result):
                check=False
                print("NO")
                break
    if (check):
        print("YES")