#a,e,i,o,u

string = "Hello Shyam, Whatsup"
count = 0
for i in string:
    if i.upper() in ['A','E','I','O','U']:
        count += 1
print(string)
print(f"Total number of vowels in a string are {count}")