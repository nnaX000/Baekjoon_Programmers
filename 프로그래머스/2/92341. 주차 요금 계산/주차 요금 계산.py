from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    extra_time = fees[2]
    extra_fee = fees[3]
    
    car_kind = set()
    cars = defaultdict(list)
    cars_fee = defaultdict(int)
    car_time = defaultdict(int)
    
    for i in fees:
        cars_fee[i] = 0
    
    for i in records:
        time,car,enter = i.split(' ')
        cars[car].append(time)
        car_kind.add(car)
        
    for key,value in cars.items():
        for i in range(0,len(value),2):
            time = 0
            if(i+1==len(value)):
                hour,minute = map(int,value[i].split(':'))
                hour = (23 - hour)*60
                minute = 59 - minute
                time = hour+minute
            else:
                start_hour, start_minute = map(int,value[i].split(':'))
                end_hour, end_minute = map(int,value[i+1].split(':'))
                hour = (end_hour - start_hour)*60
                minute = (start_minute - end_minute)
                time = hour-minute
            
            car_time[key]+=time
    
    for key,value in car_time.items():
        if(value <= basic_time):
            cars_fee[key] = basic_fee
        else:
            value -= basic_time
            value = math.ceil(value/extra_time)
            cars_fee[key] = basic_fee+value*extra_fee
    
    car_kind=list(car_kind)
    car_kind.sort()
    
    for i in car_kind:
        answer.append(cars_fee[i])
              
    return answer