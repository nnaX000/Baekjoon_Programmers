import sys

T=int(sys.stdin.readline().rstrip())
answer=[[0 for i in range(4)] for j in range(T)]

money=[25,10,5,1]

for i in range(T):

    ram=int(sys.stdin.readline().rstrip())

    for jdx,j in enumerate(money):
        answer[i][jdx]=ram//j
        ram-=(ram//j)*j

for i in answer:
    for j in i:
        print(j,end=" ")
    print()