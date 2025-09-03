import sys

N=int(sys.stdin.readline().rstrip())

tree=[[] for i in range(N+1)]

for i in range(N-1):
    x,y=map(int,sys.stdin.readline().rstrip().split(' '))
    tree[x].append(y)
    tree[y].append(x)

order=list(map(int,sys.stdin.readline().rstrip().split(' ')))

pos=[0 for i in range(N+1)]
for idx,i in enumerate(order):
    pos[i]=idx

for i in range(len(tree)):
    tree[i].sort(key=lambda x:pos[x])

real_order=[]

def dfs(u):
    global real_order

    for i in range(len(tree[u])):
        num=tree[u][i]
        if(not visited[num]):
            real_order.append(num)
            visited[num]=True
            dfs(num)


visited=[False for i in range(N+1)]
visited[1] = True
real_order.append(1)
dfs(1)

check=True

for i in range(N):
    if(order[i]!=real_order[i]):
        check=False
        print(0)
        break

if(check):
    print(1)
