def numbers():
    x=int(input("x="))
    y=int(input("y="))
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False
print(numbers())