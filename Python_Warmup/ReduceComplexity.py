# #[0,0,1,1,0,1]

li = [0,0,1,1,1,1,0,1,0,1,1,0,1]
i = 0
j = len(li)-1
while(j > i):
    print(f"i = {i}")
    print(f"j = {j}")
    if li[i] == 1 and li[j] == 0:
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
        print("swapped")
        print(li)
    if li[i] == 0:
        i += 1
    if li[j] == 1:
        j -= 1
    
print(f"li : {li}")
    
        

