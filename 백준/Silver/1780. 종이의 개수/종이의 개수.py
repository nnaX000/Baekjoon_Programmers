import sys

input=sys.stdin.readline

N=int(input())

paper=[list(map(int,input().split())) for _ in range(N)]

answer=[0,0,0]

def dfs(x,y,length):
    check=False
    stand=paper[x][y]

    for i in range(x,x+length):
        for j in range(y,y+length):
            if(paper[i][j]!=stand):
                check=True
                break

    if(not check):
        if(stand==-1):
            answer[0]+=1
        elif(stand==0):
            answer[1]+=1
        else:
            answer[2]+=1

    else:
        tmp=length//3

        dfs(x,y,tmp)
        dfs(x+tmp,y,tmp)
        dfs(x+(tmp*2),y,tmp)
        dfs(x,y+tmp,tmp)
        dfs(x,y+(tmp*2),tmp)
        dfs(x+tmp,y+tmp,tmp)
        dfs(x+(tmp*2),y+tmp,tmp)
        dfs(x+tmp,y+(tmp*2),tmp)
        dfs(x+(tmp*2),y+(tmp*2),tmp)


dfs(0,0,N)

for i in answer:
    print(i)