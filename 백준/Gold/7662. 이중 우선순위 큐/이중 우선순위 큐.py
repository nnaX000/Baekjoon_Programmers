import sys
import heapq
from collections import defaultdict

input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())

    max_heap=[]
    min_heap=[]

    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    nums=defaultdict(int)

    for j in range(n):
        order,value=input().split()
        value=int(value)

        if(order=="I"):
            heapq.heappush(max_heap,-value)
            heapq.heappush(min_heap,value)
            nums[value]+=1
        else:
            if(value==1):
                while(True and max_heap):
                    result=-heapq.heappop(max_heap)
                    if(nums[result]>0):
                        nums[result]-=1
                        break
            elif(value==-1):
                while(True and min_heap):
                    result=heapq.heappop(min_heap)
                    if(nums[result]>0):
                        nums[result]-=1
                        break

    

    if(not max_heap or not min_heap):
        print("EMPTY")
    else:
        max_value=float('-inf')
        min_value=float('inf')

        while(True and max_heap):
            result=-heapq.heappop(max_heap)
            if(nums[result]>0):
                max_value=result
                break
        
        while(True and min_heap):
            result=heapq.heappop(min_heap)
            if(nums[result]>0):
                min_value=result
                break

        if(max_value==float('-inf')):
            print("EMPTY")
        elif(min_value==float('inf')):
            print("EMPTY")
        else:
            print(max_value,min_value)