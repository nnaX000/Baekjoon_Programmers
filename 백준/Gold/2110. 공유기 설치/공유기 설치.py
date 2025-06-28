N,C = map(int,input().split(' '))
array=[]

for i in range(N):
    temp=int(input())
    array.append(temp)

array.sort()
start=1
end=max(array)-min(array)
answer=0

while(start<=end):
    pre_share=array[0]
    count=1
    mid=(start+end)//2

    for i in range(1,N):
        if(array[i]-pre_share>=mid):
            pre_share=array[i]
            count+=1

    if(count<C):
        end=mid-1
    elif(count>=C):
        answer=mid
        start=mid+1

print(answer)