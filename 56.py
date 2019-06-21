a=input()
l=list(a)
f1='False'
f2='False'
for i in range(len(l)):
    if(l[i].isdigit()):
        f1='True'
    elif(l[i].isalpha()):
        f2='True'
    else:
        c=0
if(f1 and f2 =='True'):
   print("yes")
else:
   print("no")
        
