from collections import deque
def solution(begin, target, words):
    count = 0
    dequee=deque()
    dequee.append([begin,list([begin])])
    def DFS(dequee,target,words):
        count = 0
        while(dequee):
            size=len(dequee)
            count+=1
            for i in range(size):
                tmp=dequee.popleft()
                for idx,j in enumerate(words):
                    num = 0
                    for k in range(len(j)):
                        if(j[k]==tmp[0][k]):
                            num+=1
                    if(num==len(j)-1 and (j not in tmp[1])):
                        if(j==target):
                            return count
                        else:
                            k=list(tmp[1])
                            k.append(j)
                            dequee.append([j,k])
        return 0
    return DFS(dequee,target,words)