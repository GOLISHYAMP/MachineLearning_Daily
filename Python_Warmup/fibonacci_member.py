
# 0 1 1 2 3 5 8 13

def add(a,b):
    return a+b


if __name__ == "__main__":
    num = int(input("Enter any number : "))
    li = []
    a = 0
    b = 1
    li.append(a)
    li.append(b)
    if num == 1:
        print(a)
        exit()
    if num == 2:
        print(b)
        exit()
    #li[0,1]
    # while num > b:
    #     c = a
    #     a = b
    #     b = add(c,b)
    #     # print(f"b : {b}")
    #     li.append(b)
    # print(li)
    # if num in li:
    #     print("Yes it is a member")
    # else:
    #     print("NO dost!")
    posi = 2
    while num > posi:
        c = a
        a = b
        b = add(c,b)
        # print(f"b : {b}")
        li.append(b)
        posi += 1
    print(li)
    print(li[-1])