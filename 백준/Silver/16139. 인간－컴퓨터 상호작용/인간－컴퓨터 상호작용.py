import sys
from collections import defaultdict

input=sys.stdin.readline

cumul=defaultdict(lambda : defaultdict(int))
tmp=defaultdict(int)

S=input().rstrip()
q=int(input().rstrip())

for i in range(len(S)):
    tmp[S[i]] += 1
    cumul[i] = dict(tmp)

for i in range(q):
    a,l,r=input().rstrip().split()
    l=int(l)
    r=int(r)

    if(a in cumul[r]):
        n1=cumul[r][a]
    else:
        n1=0

    if(a in cumul[l-1]):
        n2=cumul[l-1][a]
    else:
        n2=0

    print(n1-n2)