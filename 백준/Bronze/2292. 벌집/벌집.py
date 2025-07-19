import sys

N=int(sys.stdin.readline().rstrip())

tmp=1
stand=6
answer=1

while(True):
    if(N<=tmp):
        break
    tmp+=stand
    stand+=6
    answer+=1

print(answer)