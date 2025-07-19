import sys

N,B=map(int,sys.stdin.readline().rstrip().split(' '))
answer=""

while(N!=0):
    tmp=N%B
    if(tmp<10):
        answer+=str(tmp)
    else:
        answer+=chr(tmp+55)
    N//=B

answer=''.join(list(reversed(answer)))

print(answer)