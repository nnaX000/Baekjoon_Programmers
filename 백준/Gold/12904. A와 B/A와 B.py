import sys

S=sys.stdin.readline().rstrip()
T=sys.stdin.readline().rstrip()

while(True):
    tmp=T[-1]
    T=T[0:len(T)-1]
    if(tmp=="B" and len(T)>0):
        T=''.join(list(reversed(T)))

    if(S==T):
        print(1)
        break
    elif(len(T)==0):
        print(0)
        break