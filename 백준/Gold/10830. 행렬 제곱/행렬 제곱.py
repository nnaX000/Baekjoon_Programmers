import sys

input=sys.stdin.readline

N,B=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]

def calcul(array,array_1):
    tmp=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sv=0
            for k in range(N):
                sv+=(array_1[i][k]*array[k][j])
            tmp[i][j]=sv%1000
    
    return tmp

def dfs(n):
    if(n==1):
        return arr
    
    if(n%2==1):
        return calcul(dfs(1),dfs(n-1))
    else:
        a=dfs(n//2)
        return calcul(a,a)
    
answer=dfs(B)

for i in range(N):
    for j in range(N):
        answer[i][j]%=1000

for i in answer:
    print(*i)