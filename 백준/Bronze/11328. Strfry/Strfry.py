import sys
from collections import Counter

N=int(sys.stdin.readline().rstrip())

for i in range(N):
    a,b=sys.stdin.readline().rstrip().split(' ')

    a_c=Counter(a)
    b_c=Counter(b)

    result_1=a_c-b_c
    result_2=b_c-a_c

    check=False

    for key,value in result_1.items():
        if(value>0):
            check=True
            print("Impossible")
            break

    if(not check):
        for key,value in result_2.items():
            if(value>0):
                check=True
                print("Impossible")
                break

    if(not check):
        print("Possible")