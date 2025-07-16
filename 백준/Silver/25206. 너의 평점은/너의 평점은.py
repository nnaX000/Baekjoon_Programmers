import sys

score=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]

answer=0
sum_value=0

for i in range(20):
    subject, mark, grading = sys.stdin.readline().rstrip().split()

    mark=float(mark)

    if(grading!="P"):
        sum_value+=mark

    if(grading=="A+"):
        answer+=mark*score[0]
    elif(grading=="A0"):
        answer+=mark*score[1]
    elif(grading=="B+"):
        answer+=mark*score[2]
    elif(grading=="B0"):
        answer+=mark*score[3]
    elif(grading=="C+"):
        answer+=mark*score[4]
    elif(grading=="C0"):
        answer+=mark*score[5]
    elif(grading=="D+"):
        answer+=mark*score[6]
    elif(grading=="D0"):
        answer+=mark*score[7]
    elif(grading=="F"):
        answer+=mark*score[8]

print(answer/sum_value)