d1={'a':1,'b':2,'c':4}
d2={'a':3,'b':3,'d':8}
for i in d1:
    for j in d2:
        if(i==j):
            d1[i]=d1[i]+d2[j]
d2.update(d1)
print(d2)
        
