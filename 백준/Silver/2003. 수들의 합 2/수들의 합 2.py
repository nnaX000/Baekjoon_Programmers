import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

# answer=0

# for i in range(N):
#     sum_value=0
#     for j in range(i,N):
#         sum_value+=A[j]
#         if(sum_value==M):
#             answer+=1
#             break
#         if(sum_value>M):
#             break

# print(answer)

start,end=0,0
answer=0
sum_value=0

while True:
    if(sum_value>=M):
        if(sum_value==M):
            answer+=1
        sum_value-=A[start]
        start+=1
    elif(end==N):
        break
    else:
        sum_value+=A[end]
        end+=1

print(answer)