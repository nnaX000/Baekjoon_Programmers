import sys
from collections import defaultdict

input=sys.stdin.readline

cumul=defaultdict(lambda : defaultdict(int))
tmp=defaultdict(int)

S=input().rstrip()
q=int(input().rstrip())

for i in range(len(S)):
    tmp[S[i]]+=1
    k=tmp.copy()
    cumul[i]=k

for i in range(q):
    a,l,r=input().rstrip().split()
    l=int(l)
    r=int(r)

    print(cumul[r][a]-cumul[l-1][a])