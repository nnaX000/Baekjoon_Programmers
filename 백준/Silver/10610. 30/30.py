import sys

N=list(sys.stdin.readline().rstrip())

N.sort(reverse=True)

tmp=int(''.join(N))

if(tmp%30==0):
    print(tmp)
else:
    print(-1)