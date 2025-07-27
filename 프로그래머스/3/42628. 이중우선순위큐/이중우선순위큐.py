import heapq

def solution(operations):
    min_heap=[]
    max_heap=[]

    for idx,i in enumerate(operations):
        inst,num=i.split(' ')
        num=int(num)
        if(inst=="I"):
            heapq.heappush(min_heap,num)
            heapq.heappush(max_heap,-1*num)
        elif(min_heap and inst=="D" and num==1):
            tmp=heapq.heappop(max_heap)
            min_heap.remove(-1*tmp)
        elif(min_heap and inst=="D" and num==-1):
            tmp=heapq.heappop(min_heap)
            max_heap.remove(-1*tmp)

    if(min_heap):
        return [-1*heapq.heappop(max_heap),heapq.heappop(min_heap)]
    else:
        return [0,0]