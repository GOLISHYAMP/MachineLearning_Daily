def power(n,r):
    if r == 1:
        return n
    else:
        return n*power(n,r-1)
    
num = int(input("Enter a number : "))
print(power(num,4))