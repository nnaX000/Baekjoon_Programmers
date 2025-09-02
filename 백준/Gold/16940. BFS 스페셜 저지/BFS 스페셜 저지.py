import sys
from collections import deque

check=True

N=int(sys.stdin.readline().rstrip())

tree=[[] for i in range(N+1)]

for i in range(N-1):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    tree[x].append(y)
    tree[y].append(x)

order=list(map(int,sys.stdin.readline().rstrip().split(' ')))

if(order[0]!=1):
    print(0)
    sys.exit(0)

dequee=deque()

dequee.append(1)

index=1

visited=[False for i in range(N+1)]
visited[1]=True

while(dequee):
   tmp=dequee.popleft()
   candi=set()

   for i in tree[tmp]:
       if(not visited[i]):
           candi.add(i)
           
   order_candi=set(order[index:index+len(candi)])

   if(candi!=order_candi):
       print(0)
       check=False
       break
   else:
       for i in range(index,index+len(candi)):
           visited[order[i]]=True
           dequee.append(order[i])

   if(index==N-1):
       break
   else:
       index+=len(candi)

if(check):
    print(1)