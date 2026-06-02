from collections import defaultdict, Counter

n = int(input())
words = [input() for _ in range(n)]

candi=defaultdict(int)

for i in words:
    candi[tuple(sorted(Counter(i).items()))]+=1

result = sorted(candi.values(),reverse=True)

print(result[0])