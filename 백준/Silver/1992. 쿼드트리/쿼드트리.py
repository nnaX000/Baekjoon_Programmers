import sys

input=sys.stdin.readline

N=int(input())

space=[list(map(int,input().rstrip())) for _ in range(N)]
answer=""

def dfs(x,y,length):
    global answer

    check=False
    stand=space[x][y]

    for i in range(x,x+length):
        for j in range(y,y+length):
            if(stand!=space[i][j]):
                check=True
                break
    
    if(not check):
        answer+=str(stand)
    else:
        tmp=length//2
        answer+="("
        dfs(x,y,tmp)
        dfs(x,y+tmp,tmp)
        dfs(x+tmp,y,tmp)
        dfs(x+tmp,y+tmp,tmp)
        answer+=")"

dfs(0,0,N)
print(answer)