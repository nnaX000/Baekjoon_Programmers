import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

answer=[]
tree=[]

while(True):
    try:
        tmp=int(input())
        tree.append(tmp)
    except:
        break

def dfs(arr):

    if(len(arr)==0):
        return
    
    root=arr[0]
    cut=-1

    for i in range(1,len(arr)):
        if(arr[i]>root):
            cut=i
            break

    if(cut==-1):    
        cut=len(arr)
    
    dfs(arr[1:cut])
    dfs(arr[cut:len(arr)])
    answer.append(root)

dfs(tree)

for i in answer:
    print(i)