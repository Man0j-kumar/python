def addition():
    a=int(input("a="))
    b=int(input("b="))
    sum=a+b
    if sum>=15 and sum<=20:
        return 20
    else:
        print(sum)
print(addition())