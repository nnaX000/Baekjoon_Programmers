import sys

input=sys.stdin.readline

encode=input().rstrip()

N=int(input())
dic=set()
idx=1

for i in range(N):
    dic.add(input().rstrip())

while(True):
    tmp=""

    for i in encode:
        nxt=ord(i)+idx

        if(nxt>=123):
            nxt-=26
        
        tmp+=chr(nxt)
    
    for i in dic:
        if(i in tmp):
            print(tmp)
            sys.exit(0)

    idx+=1