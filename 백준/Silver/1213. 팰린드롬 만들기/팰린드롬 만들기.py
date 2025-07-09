import sys

name=list(sys.stdin.readline().strip())

avail=True

dic={}

count=0
odd_num=""
odd_count=0

answer=""

for i in name:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1

sorted_dict = dict(sorted(dic.items()))

for i in sorted_dict:
    if(sorted_dict[i]%2==1):
        count+=1
        odd_num=i
        odd_count=sorted_dict[i]
    
    if(count==2):
        avail=False
        break

if(avail):
    if(odd_count!=0):
        sorted_dict[odd_num]-=1
        answer+=odd_num
    for key, value in reversed(list(sorted_dict.items())):
        answer=key*(value//2)+answer
        answer=answer+key*(value//2)
    print(answer)
else:
    print("I'm Sorry Hansoo")