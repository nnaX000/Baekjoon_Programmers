from collections import deque

def solution(bridge_length, weight, truck_weights):
    #bridge_length : 다리에 올라갈 수 있는 트럭 수
    #weight : 다리가 견딜 수 있는 무게
    time=0
    dequee=deque(0 for i in range(bridge_length))
    trucks=deque(truck_weights)
    sum_value=0
    truck_nums=0
    real_truck=0
    
    while dequee:
        left = dequee.popleft()#여기서 하나 뺐으니까
        sum_value -= left
        time += 1

        # 2. 다음 트럭을 다리에 올릴 수 있는지 확인
        if trucks:
            if sum_value + trucks[0] <= weight:
                truck = trucks.popleft()
                dequee.append(truck)
                sum_value += truck
            else:
                dequee.append(0)  # 올라갈 트럭 없으면 자리만 차지하는 0을 넣어줘야함

    return time
    