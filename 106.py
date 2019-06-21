n=int(input())
k=int(input())
l=[]
for i in range(n):
    t=int(input())
    l.append(t)
odd=[]
for i in range(len(l)):
    if(l[i]%2!=0):
        odd.append(l[i])
print(odd[k-1])
