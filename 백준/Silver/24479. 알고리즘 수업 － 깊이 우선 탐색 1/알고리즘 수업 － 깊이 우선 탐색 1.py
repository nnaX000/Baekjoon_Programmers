import sys
node,line,start=map(int,sys.stdin.readline().split(' '))
array=[[] for i in range(node+1)]
stack=[]
for i in range(line):
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    array[tmp[0]].append(tmp[1])
    array[tmp[1]].append(tmp[0])
stack.append(start)
visited=set()
answer=[0 for i in range(node)]
index=1
for i in array:
    i.sort()
while(stack):
    target=stack.pop(-1)
    if(target not in visited):
        visited.add(target)
        answer[target-1]=index
        index+=1
        stack.extend(reversed(array[target]))
for i in answer:
    print(i)



