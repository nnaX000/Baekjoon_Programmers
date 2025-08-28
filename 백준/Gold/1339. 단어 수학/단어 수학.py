import sys

answer=0
array=[]
dic={}
max_len=0
matching={}

N=int(sys.stdin.readline())

for i in range(N):
    tmp=sys.stdin.readline()
    array.append(tmp)
    if(len(tmp)>max_len):
        max_len=len(tmp)

array.sort(key=lambda x : len(x), reverse=True)

for i in array:
    num=len(i)-1
    for j in i:
        if('A'<=j<='Z'):
            if(j not in dic):
                dic[j] = 10**num
            else:
                dic[j] += 10**num
        num-=1

final_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

value=9

for i in range(len(final_dict)):
    matching[list(final_dict.keys())[i]]=value
    value-=1

for i in array:
    tmp=""
    for j in i:
        if('A'<=j<='Z'):
            tmp+=str(matching[j])

    answer+=int(tmp)

print(answer)