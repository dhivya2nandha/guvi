s=input()
l=len(s)
v=['a','e','i','o','u']
u=[]
for i in range(l):
    if(s[i] in v):
        print(s[i],end='')
    else:
        u.append(s[i])
t=''.join(u)
print(t,end='')
