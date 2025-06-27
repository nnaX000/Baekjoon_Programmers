K, N = map(int, input().split(' '))

answer=0
array=[]

for i in range(K):
    temp=int(input())
    array.append(temp)

start=1
end=max(array)
mid=(start+end)//2

while(start<=end):
    count=0

    mid=(start+end)//2

    for i in array:
        count+=(i//mid)
    
    if(count<N):
        end=mid-1
    elif(count>=N):
        answer=max(answer,mid)
        start=mid+1

print(answer)