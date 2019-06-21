q=int(input())
q=str(q)
f=0
for i in range(0,len(q)):
  if(q[i]=='0' or q[i]=='1'):
    f=1
  else:
    f=0
    break
if(f==1):
  print("yes")
else:
    print("no")
