import sys

M=int(sys.stdin.readline().rstrip())
cluster=set()

for i in range(M):
    command=sys.stdin.readline().rstrip()
    
    if(command!="all" and command!="empty"):
        command,num=command.split(' ')
        num=int(num)

    if(command=="add"):
        cluster.add(num)
    elif(command=="remove"):
        cluster.discard(num)
    elif(command=="check"):
        if(num in cluster):
            print(1)
        else:
            print(0)
    elif(command=="toggle"):
        if(num in cluster):
            cluster.remove(num)
        else:
            cluster.add(num)
    elif(command=="all"):
        cluster=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif(command=="empty"):
        cluster=set()