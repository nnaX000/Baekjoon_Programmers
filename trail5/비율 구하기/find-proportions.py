from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

kw=defaultdict(int)

for color in words:
    kw[color]+=1

kw=dict(sorted(kw.items(),key=lambda x:x[0]))

for key,value in kw.items():
    x=value/n*100
    print(key,f"{x:.4f}")