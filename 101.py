s,n=input().split()
t=s[::-1]
l=len(t)
rev=[]
for i in range(int(n)):
    rev.append(t[i])
j=''.join(rev[::-1])
print(j)
