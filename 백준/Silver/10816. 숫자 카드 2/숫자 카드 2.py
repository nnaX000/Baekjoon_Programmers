sangNum=int(input())
dic={}
sangArray=list(map(int,input().split(' ')))
M=int(input())
testArray=list(map(int,input().split(' ')))
answer=0

for i in sangArray:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
        
for i in testArray:
    if(i in dic) :
        answer=dic[i]
    else:
        answer=0
        
    print(answer,end=" ")