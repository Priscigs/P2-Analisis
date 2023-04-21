


string1 = "matamoscasper"
string2 = "perros"

def lcs(string1, string2):
    pass




string1.upper()
string2.upper()
lx = len(string1)
ly = len(string2)



M = [[0 for x in range(ly+1)] for y in range(lx+1)]

for i in range(lx+1):
    for j in range(ly+1):
        if i == 0 or j == 0:
            M[i][j] = 0 
        elif string1[i-1] == string2[j-1]:
            M[i][j] = M[i-1][j-1] + 1
        else:
            M[i][j] = max(M[i-1][j], M[i][j-1])

index = M[lx][ly]

lsc = [""] * (index+1)
lsc[index] = ""

while lx > 0 and ly > 0:
    if string1[lx-1] == string2[ly-1]:
        lsc[index-1] = string1[lx-1]
        lx -= 1
        ly -= 1
        index -= 1
    elif M[lx-1][ly] > M[lx][ly-1]:
        lx -= 1
    else:
        ly -= 1

print(string1, string2)
print("".join(lsc))









