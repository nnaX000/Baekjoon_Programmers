import sys

N=int(sys.stdin.readline().rstrip())

tmp=set()
answer=set()

num=[1,5,10,50]

for i in range(4):
    answer.add(num[i])

for i in range(N-1):
    for j in answer:
        for k in range(4):
            tmp.add(j+num[k])
    answer=tmp
    tmp=set()

print(len(answer))