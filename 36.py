c=input()
li=list(c)
l=len(c)
count=0
for i in range(l):
    if(not(li[i].isnumeric())and not(li[i].isalpha())):
        count+=1
print(count)
