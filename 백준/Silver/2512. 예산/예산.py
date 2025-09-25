import sys

N = int(sys.stdin.readline().rstrip())
budget = list(map(int,sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())

max_value = float('-inf')

if(sum(budget)<=M):
    max_value=max(budget)
else:
    left=1
    right=max(budget)

    while(left<=right):
        tmp=[]
        middle=((left+right)//2)

        for i in range(len(budget)):
            if(middle>budget[i]):
                tmp.append(budget[i])
            else:
                tmp.append(middle)

        if(sum(tmp)<=M):
            max_value=max(max_value,max(tmp))
            left=middle+1
        else:
            right=middle-1

print(max_value)