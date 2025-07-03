N=int(input())
array=[]

for i in range(N):
    tmp=list(map(int,input().split(' ')))

    for j in tmp:
        array.append(j)

    array.sort(reverse=True)    

    if(len(array)>N):
        array=array[:N]

print(array[N-1])
