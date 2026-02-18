import sys

input=sys.stdin.readline

N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]

white=0
blue=0

def dfs(x,y,length):
    global white
    global blue

    if(length==1):
        if(paper[x][y]==0):
            white+=1
        else:
            blue+=1
        return

    check=False
    stand=paper[x][y]
    
    for i in range(length):
        for j in range(length):
            if(paper[x+i][y+j]!=stand):
                check=True
                break

    if(check):
        dfs(x,y,length//2)
        dfs(x+length//2,y,length//2)
        dfs(x,y+length//2,length//2)
        dfs(x+length//2,y+length//2,length//2)
    else:
        if(stand==0):
            white+=1
        else:
            blue+=1

dfs(0,0,N)
print(white)
print(blue)