import sys

array=[[0 for i in range(15)]for j in range(5)]

for i in range(5):
    tmp=list(sys.stdin.readline().rstrip())
    if(len(tmp)<15):
        for j in range(15-len(tmp)):
            tmp.append(-1)
    array[i]=tmp

for i in range(len(array[0])):
    for j in range(len(array)):
        if(array[j][i]!=-1):
            print(array[j][i],end="")