import sys
import heapq

input=sys.stdin.readline

T=int(input())

for i in range(T):
    M=int(input())
    arr=[]

    for j in range((M//10)+1):
        t=list(map(int,input().split()))
        arr.extend(t)

    hq=[]
    heapq.heapify(hq)
    answer=[]

    for j in range(1,M+1):
        heapq.heappush(hq,arr[j-1])

        if(j==1):
            answer.append(arr[0])
            continue
    
        if(j%2==1):
            candi=[]
            for i in range(j//2+1):
                tmp=heapq.heappop(hq)
                candi.append(tmp)

            answer.append(tmp)

            for i in range(len(candi)):
                heapq.heappush(hq,candi[i])

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i],end=" ")
        if(i==9):
            print()