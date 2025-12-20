import sys
from collections import deque

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    p=list(sys.stdin.readline().rstrip())
    dequee=deque()
    n=int(sys.stdin.readline().rstrip())
    array=sys.stdin.readline().rstrip()
    check=False
    left=True
    tmp=""

    for j in array:
        if("0"<=j<="9"):
            tmp+=j
        else:
            if(len(tmp)>0):
                dequee.append(int(tmp))
            tmp=""

    for j in p:
        if(j=="R"):
            if(left):
                left=False
            else:
                left=True
        else:
            if(dequee):
                if(left):
                    dequee.popleft()
                else:
                    dequee.pop()
            else:
                check=True
                print("error")
                break

    if(not check):
        if(len(dequee)==0):
            print("[]")
        else:
            print("[",end="")
            while(dequee):
                if(left):
                    tmp=dequee.popleft()
                else:
                    tmp=dequee.pop()

                if(len(dequee)==0):
                    print(tmp,end="]")
                else:
                    print(tmp,end=",")
            print()