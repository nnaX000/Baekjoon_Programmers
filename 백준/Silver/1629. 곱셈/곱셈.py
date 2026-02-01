import sys

input=sys.stdin.readline

A,B,C=map(int,input().split()) # (A**B)%C

def calcul(n):
    if(n==1):
        return A
    
    tmp=calcul(n//2) % C

    if(n%2==0):
        return tmp*tmp
    else:
        return tmp*tmp*calcul(1)

print(calcul(B)%C)