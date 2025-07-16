import sys

alpha=set()

alpha.add("c=")
alpha.add("c-")
alpha.add("dz=")
alpha.add("d-")
alpha.add("lj")
alpha.add("nj")
alpha.add("s=")
alpha.add("z=")

word=sys.stdin.readline().rstrip()
start=0
answer=0

while(start<len(word)):

    for i in range(3,0,-1):

        if(start+i<=len(word)):
            tmp=word[start:start+i]
        else:
            continue

        if(tmp in alpha):
            answer+=1
            start=start+i
            break
        
        if(i==1 and tmp not in alpha):
            answer+=1
            start=start+1

print(answer)