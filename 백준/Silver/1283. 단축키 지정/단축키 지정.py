import sys

N=int(sys.stdin.readline().rstrip())
alpha=[]
keys=set()
answer=[]

for i in range(N):
    alpha.append(sys.stdin.readline().rstrip())

for i in alpha:
    check=False
    tmp=list(i.split(' '))

    for jdx,j in enumerate(tmp):
        if(j[0] not in keys):
            keys.add(j[0].upper())
            keys.add(j[0].lower())
            tmp[jdx]="["+j[0]+"]"+j[1:]
            answer.append(tmp)
            check=True
            break

    if(not check):
        for jdx,j in enumerate(i):
            if("A"<=j.upper()<="Z"):
                if(j not in keys):
                    keys.add(j.upper())
                    keys.add(j.lower())
                    tmp=i[:jdx]+"["+j+"]"+i[jdx+1:]
                    answer.append([tmp])
                    check=True
                    break

    if(not check):
        answer.append([i])

for i in answer:
    tmp=""
    for j in i:
        tmp+=j
        tmp+=" "

    print(tmp)