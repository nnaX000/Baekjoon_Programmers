import sys
array=[0]*1000001#0소수 1소수 아님
array[0]=1
array[1]=1
for i in range(2,500001):
    if(array[i]==0):
        for j in range(i+i,1000001,i):
            array[j]=1
#print(array)
while(True):
    answer=""
    tmp=int(sys.stdin.readline())
    if(tmp==0):
        break
    for i in range(2,(tmp//2)+1):
        if(array[i]==0 and array[tmp-i]==0):
            answer+=str(tmp)
            answer+=" = "
            answer+=str(i)
            answer+=" + "
            answer+=str(tmp-i)
            break
    if(answer==""):
        print("Goldbach's conjecture is wrong.")
    else:
        print(answer)

