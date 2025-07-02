array=[]

try:
    for i in range(100):
        temp=input()
        if(temp==""):
            break
        array.append(temp)
except EOFError:
    pass

for i in array:
    print(i)
        