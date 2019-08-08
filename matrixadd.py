x=[[1,2],
   [2,3]]
y=[[4,3],
   [8,9]]
sum=[[0,0],
     [0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        sum[i][j]=x[i][j]+y[i][j]
for r in sum:
    print(r)
