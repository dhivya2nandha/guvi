v=['a','e','i','o','u']
s=input()
f='False'
for i in range(len(s)):
    if(s[i]in v):
        f='True'
if(f=='True'):
    print("yes")
else:
    print("no")
