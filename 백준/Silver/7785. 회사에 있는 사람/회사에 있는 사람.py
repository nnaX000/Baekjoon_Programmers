num=int(input())
array=[]
answer=set()
for i in range(num):
    temp=list(input().split(' '))
    if(temp[1]=="enter"):
        answer.add(temp[0])
    else:
        answer.remove(temp[0])
answer=sorted(answer,reverse=True)
for i in answer:
    print(i)