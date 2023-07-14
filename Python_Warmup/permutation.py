from itertools import permutations, combinations, combinations_with_replacement

li = [1,2,3]

# li1 = list(permutations(li,2))
li1  = list(combinations_with_replacement(li,2))
print(li1)

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n*fact(n-1)

# li = [1,2,3,4]

# permu = fact(len(li))
# for i in permu:
