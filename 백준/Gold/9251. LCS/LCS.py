string_1=input()
string_2=input()

table=[[0 for i in range(len(string_1)+1)] for j in range(len(string_2)+1)]


for i in range(len(string_2)):
    for j in range(len(string_1)):
        if(string_2[i]==string_1[j]):
            table[i+1][j+1]=table[i][j]+1
        else:
            table[i+1][j+1]=max(table[i+1][j],table[i][j+1])

print(table[len(string_2)][len(string_1)])