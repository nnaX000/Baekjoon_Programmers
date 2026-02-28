import sys
from collections import defaultdict

input=sys.stdin.readline

key=input().rstrip()
encode=input().rstrip()
answer=""

list=defaultdict(list)
candi=[]

for idx,i in enumerate(key):
    list[idx]=[]
    candi.append([i,idx])

candi.sort(key=lambda x:x[1])
candi.sort(key=lambda x:x[0])

idx=0
num=len(encode)//len(key)

k=0
for j,jdx in candi: #진짜 값, 순서
    count=0
    while(count<num):
        count+=1
        list[jdx].append(encode[k])
        k+=1

list=dict(sorted(list.items(),key=lambda x:x[0]))

jdx=0
for j in range(num):
    for i in range(len(key)):
        answer+=str(list[i][jdx])
    jdx+=1

print(answer)