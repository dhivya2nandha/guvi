s=input("enter string")
l=s.split()
n=len(l)
l1=[]
for i in range(n):
    t=l[i].capitalize()
    l1.append(t)
j=' '.join(l1)
print(j)
