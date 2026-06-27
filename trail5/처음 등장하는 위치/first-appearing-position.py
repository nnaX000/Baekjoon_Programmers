from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

count=defaultdict(int)

for idx,i in enumerate(arr):
    if(i not in count):
        count[i]=idx+1

count=dict(sorted(count.items(),key=lambda x:x[0]))

for key,value in count.items():
    print(key,value)