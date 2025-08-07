import sys

k=int(sys.stdin.readline().rstrip())
ho=list(sys.stdin.readline().rstrip().split(' '))

answer=[]

def dfs(tmp,num,visited):
    global answer
    get=False

    if(len(tmp)==k+1):
        answer.append(''.join(tmp))
        return

    if(len(tmp)==0):
        get=True
        for idx,i in enumerate(visited):
            tmp.append(str(idx))
            visited[idx]=True
            dfs(tmp,idx,visited)
            tmp.pop()
            visited[idx]=False
    else:
        sequence=len(tmp)-1
        if(ho[sequence]=="<"):
            for i in range(num+1,10):
                if(not visited[i]):
                    get=True
                    tmp.append(str(i))
                    visited[i]=True
                    dfs(tmp,i,visited)
                    tmp.pop()
                    visited[i]=False
        else:
            for i in range(0,num):
                if(not visited[i]):
                    get=True
                    tmp.append(str(i))
                    visited[i]=True
                    dfs(tmp,i,visited)
                    tmp.pop()
                    visited[i]=False
    
    if(not get):
        return


tmp=[]
visited=[False for i in range(10)]
dfs(tmp,0,visited)

answer.sort()

print(answer[-1])
print(answer[0])