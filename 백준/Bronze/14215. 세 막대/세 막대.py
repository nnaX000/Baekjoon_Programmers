import sys
total=0
answer=0
a,b,c=map(int,sys.stdin.readline().split())
maxx=max(a,b)
maxx=max(maxx,c)
total+=a
total+=b
total+=c
if(maxx>=total-maxx):
    answer=total-maxx+(total-maxx-1)
else:
    answer=total

print(answer)