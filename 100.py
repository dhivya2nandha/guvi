""" product of digits"""
n=int(input())
mul=1
while(n>0):
    t=n%10
    mul=mul*t
    n=n//10
print(mul)
