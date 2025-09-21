import sys
import itertools

A,B=sys.stdin.readline().rstrip().split(' ')

A_list=[]
for i in range(len(A)):
    A_list.append(A[i])

answer=-1

for i in itertools.permutations(A_list):
    if(i[0]!= str(0) and int(''.join(i))<int(B)):
        answer=max(int(''.join(i)),answer)

print(answer)