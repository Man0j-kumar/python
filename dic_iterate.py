n = int(input())          
d ={}                     
for i in range(n):        
    text = input().split()     
    d[text[0]]=int(text[1])
for i in d:
    print(i)
for i in d.values():
    print(i)
