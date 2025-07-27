import heapq

# 작업의 소요시간이 짧은 것 , 작업의 요청시각이 빠른 것, 작업 번호가 작은 것 순으로 우선순위가 높음

def solution(jobs):
    #jobs-(요청시각, 소요시간)
    task=[]
    answer=[]
    current=0
    for idx,i in enumerate(jobs):
        heapq.heappush(task,[i[1],i[0],idx]) #(소요시간,요청시간,작업번호)

    while(task):
        non_avail=[]
        avail=[]

        for i in range(len(task)):
            if(task[i][1]>current):
                non_avail.append(task[i])
            else:
                avail.append(task[i])

        heapq.heapify(avail)
        
        if(len(non_avail)==len(task)):
            current+=1
        else:
            current_task=heapq.heappop(avail)
            current+=current_task[0]
            answer.append(current-current_task[1])
            task.remove(current_task)

    return sum(answer)//len(answer)