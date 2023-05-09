#swapping two numbers without using third variable

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(f"Values before swapping is a : {a} and b : {b}")
a,b = b,a
print(f"Values after swapping is a : {a} and b : {b}")