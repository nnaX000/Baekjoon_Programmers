notHear,notSee=map(int,input().split(' '))
notHearPerson=set()
notSeePerson=set()
for i in range(notHear):
    tmp=input()
    notHearPerson.add(tmp)
for i in range(notSee):
    tmp=input()
    notSeePerson.add(tmp)
result=sorted(notHearPerson&notSeePerson)
print(len(result))
for i in result:
    print(i)