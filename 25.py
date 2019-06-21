n=int(input())
l=list(map(int,input().split()))
l.sort()
a=n//2
if(n%2!=0):
    print(l[a])
else:
    print((l[a-1]+l[a+1])/2.0)
