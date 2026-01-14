import sys

input=sys.stdin.readline

A,B=input().split()
cnt=1

while(int(B)>=int(A)):
    if(B==A):
        print(cnt)
        sys.exit(0)

    if(int(B)%2==0):
        B=int(B)
        B//=2
        B=str(B)
    elif(B[-1]=="1"):
        B=B[:len(B)-1]
    else:
        print(-1)
        sys.exit(0)

    cnt+=1

print(-1)