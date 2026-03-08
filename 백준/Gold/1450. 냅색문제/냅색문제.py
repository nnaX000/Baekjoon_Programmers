import sys
from bisect import bisect_right

input=sys.stdin.readline

N,C=map(int,input().split()) # N개의 물건, 최대 C만큼의 무게를 넣을 수 있는 가방
items=list(map(int,input().split()))

answer=0
half=N//2
items_a=items[:half]
items_b=items[half:len(items)]

def calcul(array):
    sum_v=[0]
    for i in array:
        sum_v+=[i+s for s in sum_v]
    return sum_v

itemA=calcul(items_a)
itemB=calcul(items_b)
itemB.sort()

for i in itemA:
    if(i<=C):
        answer+=bisect_right(itemB,C-i)

print(answer)