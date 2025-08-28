import sys

N=int(sys.stdin.readline().rstrip())
W=list(map(int,sys.stdin.readline().rstrip().split(' ')))

max_value=float('-inf')

def dfs(W,cost):
    global max_value

    if(len(W)==2):
        if(cost>max_value):
            max_value=cost
        return

    for i in range(1,len(W)-1):
        cost+=(W[i-1]*W[i+1])
        new_w=W[:]
        new_w.pop(i)
        dfs(new_w,cost)
        cost-=(W[i-1]*W[i+1])

dfs(W,0)
print(max_value)