import sys
from collections import defaultdict
import heapq

input=sys.stdin.readline

T=int(input())

for i in range(T):
    k=int(input())

    #‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 
    # 동일한 정수가 삽입될 수 있음을 참고하기 바란다. 
    # ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미

    max_q=[] #-로 넣어야 함.
    min_q=[] #그대로 넣어야 함.

    heapq.heapify(max_q)
    heapq.heapify(min_q)

    nums=defaultdict(int) # 상태관리

    for i in range(k):
        inst,n=input().split()
        n=int(n)

        if(inst=="I"):
            nums[n]+=1
            heapq.heappush(max_q,-n)
            heapq.heappush(min_q,n)
        else:
            if(n==1 and max_q):
                tmp=-heapq.heappop(max_q)

                while(tmp not in nums and max_q):
                    tmp=-heapq.heappop(max_q)

                if(tmp in nums):
                    nums[tmp]-=1
                    if(nums[tmp]==0):
                        del nums[tmp]

            elif(n==-1 and min_q):
                tmp=heapq.heappop(min_q)

                while(tmp not in nums and min_q):
                    tmp=heapq.heappop(min_q)

                if(tmp in nums):
                    nums[tmp]-=1
                    if(nums[tmp]==0):
                        del nums[tmp]

        # print("max_q",max_q)
        # print("min_q",min_q)
        # print("nums",nums)

    if(len(nums)==0):
        print("EMPTY")
    else:
        max_value=float('-inf')
        min_value=float('inf')

        for key,value in nums.items():
            max_value=max(max_value,key)
            min_value=min(min_value,key)

        print(max_value,min_value)