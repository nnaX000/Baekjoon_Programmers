import math
from itertools import product

def solution(n):
    answer = ''
    
    while(n>0):
        n-=1
        n,r=divmod(n,3) #나머지가 0,1,2 셋 중에 하나로 나옴
        answer = '124'[r] + answer
    
    return answer