a,b,c=input().split()
if(a==b==c):
    print("All are equal")
elif(a>b and a>c):
    print(a,"is greater")
elif(b>c and b>a):
    print(b,"is greater")
else:
    print(c,"is greater")
