import math
str1 = "vikesh shrivastav"

rows = 5
posi = 0
for i in range(1,rows+1):
    count = 1 + (2*(i-1))
    rows = rows -1
    p = " "*rows
    
    while(count > 0 and posi < len(str1)):
        p += str1[posi]
        posi += 1
        count -= 1
    print(p)
