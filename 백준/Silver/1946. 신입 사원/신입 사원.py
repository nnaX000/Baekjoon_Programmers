T=int(input())
answer=[]

for i in range(T):

    accept=[]
    array=[]

    N=int(input())

    for j in range(N):
        array.append(list(map(int,input().split(' '))))

    array.sort(key=lambda x:x[0])
    accept.append(array[0])
    max_second=array[0][1]

    min_value=[float('inf')]

    array.sort(key=lambda x:x[1])

    for k in range(max_second-1):
        if(min_value[0]>array[k][0]):
            accept.append(array[k])
            min_value[0]=min(min_value[0],array[k][0])

    answer.append(len(accept))

for i in answer:
    print(i)