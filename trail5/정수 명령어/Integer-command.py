from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    s = SortedSet()
    
    for a,b in operations:
        if(a == "I"):
            s.add(int(b))
        elif(a == "D"):
            if(int(b)==1 and s):
                tmp=s[-1]
                s.remove(tmp)
            elif(int(b)==-1 and s):
                tmp=s[0]
                s.remove(tmp)

    if(not s):
        print("EMPTY")
    else:
        print(s[-1],s[0])