import sys

N,M,R=map(int,sys.stdin.readline().rstrip().split(' '))
A=[]
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

command=list(map(int,sys.stdin.readline().rstrip().split(' ')))

def one():
    tmp=[]
    tmp=list(reversed(A))

    return tmp

def two():
    tmp=[]
    for i in range(len(A)):
        tmp.append(list(reversed(A[i])))

    return tmp

def three():
    tmp=[]
    for i in range(len(A[0])):
        tmp_1=[]
        for j in range(len(A)-1,-1,-1):
            tmp_1.append(A[j][i])
        tmp.append(tmp_1)

    return tmp

def four():
    tmp=[]
    for i in range(len(A[0])-1,-1,-1):
        tmp_1=[]
        for j in range(len(A)):
            tmp_1.append(A[j][i])
        tmp.append(tmp_1)

    return tmp

def five():
    tmp=[]
    start=0
    end=len(A[0])//2
    for j in range(len(A)//2):
        tmp_1=[]
        tmp_1.extend(A[j+(len(A)//2)][start:end])
        tmp_1.extend(A[j][start:end])

        tmp.append(tmp_1)

    start=len(A[0])//2
    end=len(A[0])
    for j in range(len(A)//2):
        tmp_1=[]
        tmp_1.extend(A[j+(len(A)//2)][start:end])
        tmp_1.extend(A[j][start:end])

        tmp.append(tmp_1)

    return tmp

def six():
    tmp=[]
    start=len(A[0])//2
    end=len(A[0])
    for j in range(len(A)//2):
        tmp_1=[]
        tmp_1.extend(A[j][start:end])
        tmp_1.extend(A[j+(len(A)//2)][start:end])

        tmp.append(tmp_1)

    start=0
    end=len(A[0])//2
    for j in range(len(A)//2):
        tmp_1=[]
        tmp_1.extend(A[j][start:end])
        tmp_1.extend(A[j+(len(A)//2)][start:end])

        tmp.append(tmp_1)
        
    return tmp

for i in command:
    if(i==1):
        result=one()
    elif(i==2):
        result=two()
    elif(i==3):
        result=three()
    elif(i==4):
        result=four()
    elif(i==5):
        result=five()
    elif(i==6):
        result=six()

    A = [row[:] for row in result]

for i in A:
    print(*i)