import sys

X,Y=map(int,sys.stdin.readline().rstrip().split(' '))
score=100 * Y // X

if(score==100 or score==99):
    print(-1)
else:
    min_value=float('inf')
    left=1
    right=10000000000000000

    while(left<=right):
        middle=(left+right)//2
        tmp=100*(Y+middle)//(X+middle)

        if(tmp>score):
            min_value=min(min_value,middle)
            right=middle-1
        else:
            left=middle+1

    print(min_value)