import sys
while(True):
    maxx=0
    total=0
    answer=""
    a,b,c=map(int,sys.stdin.readline().split())
    if(a==0 and b==0 and c==0):
        break
    maxx=max(a,b)
    maxx=max(maxx,c)
    total+=a
    total+=b
    total+=c
    if(maxx>=total-maxx):
        answer="Invalid"
    else:
        if(a==b==c):
            answer="Equilateral"
        elif(a!=b and a!=c and b!=c):
            answer="Scalene"
        else:
            answer="Isosceles"
    print(answer)