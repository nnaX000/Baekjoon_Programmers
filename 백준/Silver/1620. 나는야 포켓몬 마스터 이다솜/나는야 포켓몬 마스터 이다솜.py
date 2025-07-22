import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

pocket=dict()
reversed_pocket=dict()
num=1

for i in range(N):
    tmp=sys.stdin.readline().rstrip()
    pocket[tmp]=num
    reversed_pocket[num]=tmp
    num+=1

for i in range(M):
    tmp=sys.stdin.readline().rstrip()
    if("A"<=tmp[0]<="Z" or "A"<=tmp[-1]<="Z"):
        print(pocket[tmp])
    else:
        print(reversed_pocket[int(tmp)])