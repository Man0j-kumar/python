#Python program to convert a tuple to a dictionary
tup=((2,'w'),(3,'r'))
print(dict((x,y)for y,x in tup))