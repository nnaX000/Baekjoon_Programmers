N, M = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

start=max(array)
end=sum(array)
min_value=[float('inf')]
temp=0

while(start<=end):
    count=1
    temp=0
    mid=(start+end)//2

    for i in array:
        if(temp+i>mid):
            temp=i
            count+=1
        else:
            temp+=i

    if(count<=M):
        min_value[0]=mid
        end=mid-1
    else:
        start=mid+1

print(min_value[0])

