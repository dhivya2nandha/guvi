n=int(input())
f='False'
for i in range(2,n):
    if(n%i==0):
        f='True'
    else:
        f='False'
if(f=='True'):
    print("prime")
else:
    print("not prime")
