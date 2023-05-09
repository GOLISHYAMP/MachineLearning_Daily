#HCF of two numbers is 6 and 35 is 

n,m = list(map(int,input("Enter the two numbers is : ").split()))
smallest = n if n<m else m
# print(smallest)
for i in range(2,smallest+1):
    if i == smallest:
        i = 1
        break
    if (n%i == 0 and m%i == 0):
        break
print(f"HCF of two numbers {m} and {n} is : {i}")