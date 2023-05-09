#LCM of 2 and 3 is 6,  5 and 9 is 45

n,m = list(map(int,input("Enter two numbers : ").split()))
largest = m if m>n else n
smallest = m if n==largest else n
if largest%smallest == 0:
    print(f"LCM of {largest} and {smallest} is {largest}")
i = 1
while (largest*i)%smallest != 0:
    i += 1 
print(f"LCM of {largest} and {smallest} is {largest*i}")