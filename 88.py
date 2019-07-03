nn,mm=map(int,input().split())
a=nn
b=mm
while(mm):
  nn,mm=mm,nn%mm
  c=(a*b)//nn
print(c)
