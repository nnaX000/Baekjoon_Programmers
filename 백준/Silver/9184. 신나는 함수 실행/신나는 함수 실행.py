import sys

input=sys.stdin.readline

dp=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def dfs(x,y,z):
    if(x<=0 or y<=0 or z<=0):
        return 1
    
    if(x<y and y<z):
        return dp[x][y][z-1] if dp[x][y][z-1]!=0 else dfs(x,y,z-1)  + dp[x][y-1][z-1] if dp[x][y-1][z-1]!=0 else dfs(x,y-1,z-1) - dp[x][y-1][z] if dp[x][y-1][z]!=0 else dfs(x,y-1,z)
    
    return (dp[x-1][y][z] if dp[x-1][y][z]!=0 else dfs(x-1,y,z)) + (dp[x-1][y-1][z] if dp[x-1][y-1][z]!=0 else dfs(x-1,y-1,z)) + (dp[x-1][y][z-1] if dp[x-1][y][z-1]!=0 else dfs(x-1,y,z-1)) - (dp[x-1][y-1][z-1] if dp[x-1][y-1][z-1]!=0 else dfs(x-1,y-1,z-1))

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            result=dfs(i,j,k)
            dp[i][j][k]=result

while(True):
    a,b,c=map(int,input().split())
    answer=0

    if(a==-1 and b==-1 and c==-1):
        break

    if(a<=0 or b<=0 or c<=0):
        answer=1
    elif(a>20 or b>20 or c>20):
        answer=dp[20][20][20]
    else:
        answer=dp[a][b][c]

    print("w("+str(a)+", "+str(b)+", "+str(c)+") =",answer)