import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    array=[]

    for j in range(n):
        array.append(input().rstrip())

    array.sort()

    check=False

    for i in range(len(array)-1):
        stand=array[i]
        stand_1=array[i+1][:len(array[i])]
        if(stand==stand_1):
            check=True
            break

    if(not check):
        print("YES")
    else:
        print("NO")