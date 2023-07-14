# str1 = "kaiS"
# str2 = "saik"

# dic1 = {}
# dic2 = {}
# for i in str1:
#     dic1[i] = str1.count(i)
# # print(dic1)
# for i in str2:
#     dic2[i] = str2.count(i)
# # print(dic2)

# if len(dic1) != len(dic2):
#     print("Didn't Have same Number of letters")
#     print("NOT SAME")
#     exit()

# if dic1.keys() != dic2.keys():
#     print("Didn't Have same letters")
#     print("NOT SAME")
#     exit()

# for i in str1:
#     if dic1[i] != dic2[i]:
#         print("NOT SAME")
#         exit()

# print("SAME STRINGS")

# li = "saikrushna"
# temp = [i for i in li]
# print(temp)

# print(''.join(temp))


str1 = "Hello Sai how are you"
# res = "olleH iaS woh era uoy"

li = str1.split(" ")
# print(li)
temp = []
for i in li:
    temp.append(i[::-1])
# print(temp)
print(' '.join(temp))