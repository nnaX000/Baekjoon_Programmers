import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    N=int(sys.stdin.readline().rstrip())
    one=set(map(int,sys.stdin.readline().rstrip().split(' ')))
    M=int(sys.stdin.readline().rstrip())
    two=list(map(int,sys.stdin.readline().rstrip().split(' ')))

    for j in two:
        if(j in one):
            print(1)
        else:
            print(0)