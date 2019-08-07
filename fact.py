n=int(input("enter a number:"))
fact=1
if n<0:
    print("factorial doesn't exist")
elif n==0:
    print("factorial for 0 is 1")
else:
    while n>0:
        fact=fact*n
        n=n-1
    print("factorial=",fact)