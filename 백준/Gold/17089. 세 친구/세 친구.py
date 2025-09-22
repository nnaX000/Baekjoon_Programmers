import sys
import itertools
from collections import defaultdict

N, M = map(int,sys.stdin.readline().rstrip().split(' '))

relation = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(M)]
min_value=float('inf')
candi=[i for i in range(1,N+1)]
candi_dict = defaultdict(set)

for i in relation:
    a,b=i[0],i[1]
    candi_dict[a].add(b)
    candi_dict[b].add(a)

for k in candi_dict :
    for a,b in itertools.combinations(candi_dict[k],2):
        c = int(k)

        array=[a,b,c]

        if (not b in candi_dict[a]):
            continue
        
        tmp=0

        for j in range(3):
            tmp+=len(candi_dict[array[j]])

            if(j==0):
                if(array[1] in candi_dict[array[j]]):
                    tmp-=1
                if(array[2] in candi_dict[array[j]]):
                    tmp-=1

            if(j==1):
                if(array[0] in candi_dict[array[j]]):
                    tmp-=1
                if(array[2] in candi_dict[array[j]]):
                    tmp-=1

            if(j==2):
                if(array[0] in candi_dict[array[j]]):
                    tmp-=1
                if(array[1] in candi_dict[array[j]]):
                    tmp-=1

        min_value = min(min_value,tmp)

print(min_value if min_value != float('inf') else -1)