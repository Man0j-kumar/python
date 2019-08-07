a=[int(x) for x in input().split()[:4]]
b=int(input())
c=min(a)
if(c>b):
  print("all are greater")
else:
  print("all are not greater")