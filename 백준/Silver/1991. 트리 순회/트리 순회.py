import sys
from collections import defaultdict

input=sys.stdin.readline

N=int(input())
tree=defaultdict(list)

for i in range(N):
    root,left,right=input().split()

    tree[root]=[left,right]

def preOrder(n):
    if(n=="."):
        return
    print(n,end="")
    preOrder(tree[n][0])
    preOrder(tree[n][1])

preOrder("A")
print()

def middleOrder(n):
    if(n=="."):
        return
    middleOrder(tree[n][0])
    print(n,end="")
    middleOrder(tree[n][1])

middleOrder("A")
print()

def postOrder(n):
    if(n=="."):
        return
    postOrder(tree[n][0])
    postOrder(tree[n][1])
    print(n,end="")

postOrder("A")