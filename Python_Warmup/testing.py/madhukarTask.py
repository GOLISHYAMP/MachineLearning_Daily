arr1 = ['s','h','y','a','m']
arr2 = ['g','o','l','i']
len_final = len(arr1)+len(arr2)+1
final = [' ']*len_final
print(final)
for i in range(len(arr1)):
    final[i] = arr1[i]
print(final)
for i in range(len(arr1)+1,len(final)):
    final[i] = arr2[i-(len(arr1)+1)]

print(final)
print(''.join(final))
