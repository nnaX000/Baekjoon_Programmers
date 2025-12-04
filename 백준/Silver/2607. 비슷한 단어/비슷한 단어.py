import sys
from collections import Counter

#두개의 단어가 같은 종류의 문자로 이루어져 있다.
#같은 문자는 같은 개수만큼 있다

#한문자 더하거나 빼거나 하나의 문자를 다른 문자로 바꾸기

N=int(sys.stdin.readline().rstrip())
stand=""
candi=[]

answer=0

for i in range(N):
    if(i==0):
        stand=sys.stdin.readline().rstrip()
        stand_1=Counter(stand)
    else:
        tmp=sys.stdin.readline().rstrip()
        tmp_1=Counter(tmp)
        sum_value=0
        
        diff_1=stand_1-tmp_1
        diff_2=tmp_1-stand_1

        sum_value+=sum([value for value in diff_1.values()])
        sum_value+=sum([value for value in diff_2.values()])

        if(len(tmp)==len(stand)):
            if(sum_value<=2):
                answer+=1
        elif(abs(len(tmp)-len(stand))==1):
            if(sum_value==1):
                answer+=1

print(answer)