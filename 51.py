n=int(input())
l=[]
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
a=l[::-1]
for i in range(len(a)):
    print(a[i],end=' ')
