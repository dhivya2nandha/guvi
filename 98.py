n=int(input())
t=[]
for i in range(n):
    l=int(input())
    t.append(l)
c=t[0]
for i in range(n):
    if(t[i]!=c):
        print(i)
        break
    c+=1
