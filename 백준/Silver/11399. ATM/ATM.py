answer=0
sum=0
num=int(input())
people=list(map(int,input().split(' ')))
people=sorted(people)
for i in people:
    sum+=i
    answer+=sum
print(answer)