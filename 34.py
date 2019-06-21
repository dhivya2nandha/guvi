s=input()
l1=list(s)
l=len(l1)
count=0
for i in range(l):
    if(l1[i]=="."):
        count+=1
print(count)
