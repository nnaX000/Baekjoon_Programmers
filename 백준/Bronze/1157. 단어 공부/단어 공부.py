import sys

max_value=0

word=dict()

w=sys.stdin.readline().rstrip()

answer=""

for i in w:
    tmp=i
    num_tmp=int(ord(tmp))
    if(ord(i)>90):
        num_tmp-=32

    tmp=chr(num_tmp)

    if(tmp in word):
        word[tmp]+=1
    else:
        word[tmp]=1

count=1
max_value=max(word.values())
aligned_word=sorted(word.items() ,key=lambda x:x[1],reverse=True)

for k,v in word.items():
    if(max_value==v):
        count+=1
    if(count==3):
        answer="?"
        break

if(answer!="?"):
    answer=aligned_word[0][0]

print(answer)
