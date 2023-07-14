k = ["vikes", "vikeshs", "keshvi", "ikes", "mukesh"]
len_list = list(len(i) for i in k)
max_window = min(len_list)
string = list(i for i in k if len(i) == max_window)[0]
print(string)
print(max_window)
loop = max_window
found = False

for i in range(loop):
    max_window =  loop - i
    for j in k:
        jump = False
        string = string[i:loop]
        print(f"String is {string}")
        for l in range(0, len(j)-max_window+1):
            if j[l:l+max_window] == string:
                print("OK")
                jump = True
                break
        if not jump:
            break
        if jump and j==k[-1]:
            print(string)
