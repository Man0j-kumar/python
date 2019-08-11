#Python program to find the repeated items of a tuple
a=input().split()
b=tuple(a)
s=set(b)
for i in s:
    c=b.count(i)
    if(c>1):
        print(i)
