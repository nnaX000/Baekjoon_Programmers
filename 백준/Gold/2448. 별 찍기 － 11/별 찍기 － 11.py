import sys

input=sys.stdin.readline

N=int(input())
star=[[" " for _ in range(N*2)] for _ in range(N)]

def dfs(height,x,y):
    if(height==3):
        star[x][y]="*"
        star[x+1][y-1]="*"
        star[x+1][y+1]="*"
        for i in range(-2,3,1):
            star[x+2][y+i]="*"
        return

    dfs(height//2,x,y)
    dfs(height//2,x+height//2,y-height//2)
    dfs(height//2,x+height//2,y+height//2)

dfs(N,0,N-1)

for i in star:
    for j in i:
        print(j,end="")
    print()