import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,B=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]

def calcul(a,b):
    result=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N): #좌표
            for k in range(N):
                result[i][j]+=(a[i][k]*b[k][j])%1000

    return result

twice=calcul(A,A)

def answer(n):
    if(n==1):
        return A
    
    if(n%2==1):
        half=answer((n-1)//2)
        return calcul(calcul(A,half),half)
    else:
        half=answer(n//2)
        return calcul(half,half)
    
for i in answer(B):
    for j in i:
        print(j%1000,end=" ")
    print()