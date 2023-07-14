B = { "{" : "}", "[" : "]", "(" : ")"}
inp = "{{[([)]}}{[}]}"
temp = []
for i in inp:
    if i in B:
        temp.append(i)