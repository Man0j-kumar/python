a=[int(x) for x in input().split()]
p,i=2,0
while(len(a)>0):
    i=(i+p)%len(a)
    print(a.pop(i))
    
    
    
    

    

    
