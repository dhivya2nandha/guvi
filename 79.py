import math
n,m=list(map(int,input().split()))
c=n*m
root=math.sqrt(c)
if (int(root+0.5)**2==c):
  print("yes")
else:
  print("no")
