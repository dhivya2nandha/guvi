c=input()
li=list(c)
l=len(c)
count=0
for i in range(l):
    if(li[i].isnumeric()):
        count+=1
print(count)
