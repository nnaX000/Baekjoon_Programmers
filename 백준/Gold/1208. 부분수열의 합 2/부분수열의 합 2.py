import sys
from collections import defaultdict

N,S=map(int,sys.stdin.readline().rstrip().split(' '))
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

def dfs(array,start,sum_value,dic):

    for i in range(start,len(array)):
        sum_value+=array[i]
        dic[sum_value]+=1
        dfs(array,i+1,sum_value,dic)
        sum_value-=array[i]

    return dic

answer=0

left=A[:N//2]
right=A[N//2:]

left_dic=defaultdict(int)
right_dic=defaultdict(int)

left_result=dfs(left,0,0,left_dic)
right_result=dfs(right,0,0,right_dic)
left_result[0]+=1
right_result[0]+=1

for key,value in left_result.items():
    answer += value * right_dic.get(S - key, 0)

if(S==0):
    answer-=1
    
print(answer)