from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

count=defaultdict(int)

for i in words:
    count[i]+=1

count=dict(sorted(count.items(),key=lambda x:x[0]))

for k,v in count.items():
    print(k,v)