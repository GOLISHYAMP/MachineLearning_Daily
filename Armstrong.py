def cube(num):
    return num*num*num

n = int(input("Enter the number : "))
sum = 0
t = n
while n>0:
    sum += cube(n%10)
    n = n//10
if sum == t:
    print("Yeah! it is a Armstrong")
else:
    print("Oooh!, it is not a Armstrong Number")