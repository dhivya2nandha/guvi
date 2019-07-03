x=list(input())
y=[]
for i in x:
   if i not in y:
      y.append(i)
if x==y:
   print("Yes")
else:
print("No")
