import sys

A,B=sys.stdin.readline().rstrip().split(' ')

answer=1
success=False

while(B!=""):
    if(int(B)%2==0):
        B=int(B)
        B//=2
        B=str(B)
    elif(B[-1]=="1"):
        B=B[:len(B)-1]
    else:
        break
    
    answer+=1

    if(A==B):
        success=True
        break

if(success):
    print(answer)
else:
    print(-1)