num=int(input())
score=''
if(num<=100 and num>=90):
    score="A"
elif(num<=89 and num>=80):
    score="B"
elif(num<=79 and num>=70):
    score="C"
elif(num<=69 and num>=60):
    score="D"
else:
    score="F"
print(score)