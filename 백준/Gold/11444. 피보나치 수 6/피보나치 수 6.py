import sys

input=sys.stdin.readline

n=int(input())

def calcul(k,m):
    result=[[0,0],[0,0]]

    result[0][0]=(k[0][0]*m[0][0]+k[0][1]*m[1][0])%1000000007
    result[0][1]=(k[0][0]*m[0][1]+k[0][1]*m[1][1])%1000000007
    result[1][0]=(k[0][0]*m[1][0]+k[1][0]*m[1][1])%1000000007
    result[1][1]=(k[0][1]*m[1][0]+k[1][1]*m[1][1])%1000000007

    return result

def fibo(n):
    if(n==1):
        return [[1,1],[1,0]]
    
    half=fibo(n//2)
    h_r=calcul(half,half)

    if(n%2==0):
        return h_r
    else:
        return calcul(h_r,[[1,1],[1,0]])
    
result=fibo(n)

for i in range(2):
    for j in range(2):
        result[i][j]%=1000000007

print(result[1][0])