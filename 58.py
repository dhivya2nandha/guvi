n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(len(l)):
    if(l[i]==k):
        c+=1
if(c>=1):
    print("yes")
else:
    print("no")
