# Sorted list is available we have to remove multiple occurence which is having more than 2 occurance

li = [1,2,2,3,3,3,4,5,5,5,6,6,6]

res = []
temp = set(li)
# print(temp)
for i in temp:
    if li.count(i) < 3:
        t = [i]*li.count(i)
        res.append(t)
    else:
        res.extend([i,i])
print(res) 