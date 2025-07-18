import sys

while(True):
    tmp=int(sys.stdin.readline().rstrip())
    sum_value=0
    array=[]
    if(tmp!=-1):
        for i in range(1,int(tmp**(1/2)+1)):
            if(tmp%i==0):
                sum_value+=i
                array.append(i)
                if(i!=tmp//i and tmp//i!=tmp):
                    sum_value+=tmp//i
                    array.append(tmp//i)

        array.sort()
        
        if(sum_value==tmp):
            print(tmp,"=",end=" ")
            for idx,i in enumerate(array):
                if(idx!=len(array)-1):
                    print(i,end=" + ")
                else:
                    print(i)
        else:
            print(tmp,"is NOT perfect.")

    else:
        break