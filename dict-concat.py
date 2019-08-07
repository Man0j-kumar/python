# Python program to concatenate following dictionaries to create a new one
d1={1:2,3:4}
d2={5:6,7:9}
d3={10:8,13:22} 
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print(d4)