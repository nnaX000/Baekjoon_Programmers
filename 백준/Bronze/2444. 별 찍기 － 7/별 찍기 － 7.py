import sys

N=int(sys.stdin.readline().rstrip())

stand=1
space=N-1

for i in range(N):
    print(" "*space,end="")
    print("*"*stand,end="")
    stand+=2
    space-=1
    print()


stand-=4
space+=2

for j in range(N-1):
    print(" "*space,end="")
    print("*"*stand,end="")
    stand-=2
    space+=1
    print()
