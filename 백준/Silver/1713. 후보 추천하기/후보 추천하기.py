import sys
from collections import defaultdict

N=int(sys.stdin.readline().rstrip()) #후보수
num=int(sys.stdin.readline().rstrip()) #추천횟수
nums=list(map(int,sys.stdin.readline().rstrip().split(' ')))

candi=defaultdict(int)

for i in nums:
    if(i in candi):
        candi[i]+=1
    else:
        if(len(candi)<N):
            candi[i]+=1
        elif(len(candi)==N):
            n_c=sorted(candi.items(),key=lambda x:x[1])
            del candi[n_c.pop(0)[0]]
            candi[i]+=1

n_c=sorted(candi.items(),key=lambda x:x[0])
for key,value in n_c:
    print(key,end=" ")