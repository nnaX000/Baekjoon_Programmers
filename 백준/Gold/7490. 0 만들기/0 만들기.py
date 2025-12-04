import sys
from itertools import product
import re

case=int(sys.stdin.readline().rstrip())

for i in range(case):
    N=int(sys.stdin.readline().rstrip())

    candi=[i for i in range(1,N+1)]
    method=list(product([" ","+","-"],repeat=N-1))
    
    for j in method:
        tmp="1"
        num=2
        for k in j:
            tmp+=k
            tmp+=str(num)
            num+=1
        
        origin=tmp
        tmp_1=tmp.replace(" ","")
        
        tmp_2=re.split(r"([+\-*])", tmp_1)

        sum_value=int(tmp_2[0])
        
        for i in range(2,len(tmp_2),2):
            if(tmp_2[i-1]=="+"):
                sum_value+=int(tmp_2[i])
            else:
                sum_value-=int(tmp_2[i])

        if(sum_value==0):
            print(''.join(origin))

    print()