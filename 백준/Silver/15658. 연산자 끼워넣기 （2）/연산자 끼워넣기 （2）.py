import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
buho=list(map(int,sys.stdin.readline().rstrip().split(' ')))

max_value=float('-inf')
min_value=float('inf')

def calculate(sum_value,target):
    global max_value
    global min_value

    if(sum(buho)==0 or target>=len(A)):
        if(sum_value<min_value):
            min_value=sum_value
        
        if(sum_value>max_value):
            max_value=sum_value

        return

    for idx,i in enumerate(buho):
        if(i>0):
            if(idx==0):
                sum_value+=A[target]
                target+=1
                buho[idx]-=1
                calculate(sum_value, target)
                target-=1
                sum_value-=A[target]
                buho[idx]+=1
            elif(idx==1):
                sum_value-=A[target]
                target+=1
                buho[idx]-=1
                calculate(sum_value, target)
                target-=1
                sum_value+=A[target]
                buho[idx]+=1
            elif(idx==2):
                sum_value*=A[target]
                target+=1
                buho[idx]-=1
                calculate(sum_value, target)
                target-=1
                sum_value//=A[target]
                buho[idx]+=1
            elif(idx==3):
                check=False
                if(sum_value<0):
                    sum_value=-1*sum_value
                    check=True
                sum_value//=A[target]
                target+=1
                buho[idx]-=1
                if(check):
                    sum_value=-1*sum_value
                calculate(sum_value, target)
                target-=1
                sum_value*=A[target]
                buho[idx]+=1
                check=False

calculate(A[0],1)
print(int(max_value))
print(int(min_value))