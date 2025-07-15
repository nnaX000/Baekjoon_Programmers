import sys

alpa=['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

num=sys.stdin.readline().rstrip()

answer=0

for i in num:
    for jdx,j in enumerate(alpa):
        if(i in j):
            answer+=(jdx+1)
            break

print(answer)