from functools import cmp_to_key

def compare(x,y):
    if(x+y>y+x):
        return -1
    elif(x+y<y+x):
        return 1
    else:
        return 0


def solution(numbers):
    new_numbers=[]
    for i in numbers:
        i=str(i)
        new_numbers.append(i)

    new_numbers.sort(key=cmp_to_key(compare))

    if(new_numbers[0]=='0'):
        return "0"

    return ''.join(new_numbers)
