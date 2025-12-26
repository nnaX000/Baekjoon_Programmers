import sys

input=sys.stdin.readline

K,N=map(int,input().split(' '))

answer=0
array=[]

for i in range(K):
    array.append(int(input()))

left=1
right=max(array)

while(left<=right):
    middle=(left+right)//2
    sum_value=0

    if(middle!=0):
        for i in range(K):
            sum_value+=array[i]//middle

        if(sum_value<N):
            right=middle-1
        else:
            answer=middle
            left=middle+1

print(answer) 