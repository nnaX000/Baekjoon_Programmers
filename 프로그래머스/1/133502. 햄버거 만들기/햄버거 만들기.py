from collections import deque

def solution(ingredient):
    answer=0
    a=""
    for i in ingredient:
        a+=str(i)
        if(a[-4:]=='1231'):
            a=a[0:len(a)-4]
            answer+=1
    #빵 – 야채 – 고기 - 빵
    #1 -  2  -  3  - 1
    return answer