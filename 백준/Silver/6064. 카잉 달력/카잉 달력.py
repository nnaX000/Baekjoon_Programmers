import sys
import math

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    year=0
    exist=False
    observed_x=set()
    observed_y=set()

    M,N,x,y=map(int,sys.stdin.readline().rstrip().split(' '))

    limit=math.lcm(M,N)

    j=x

    while(j<=limit):
        if((j-y)%N==0):
            print(j)
            exist=True
            break
        j+=M

    if(not exist):
        print(-1)