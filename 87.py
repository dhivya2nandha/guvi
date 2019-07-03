
"""87.py"""
xx,yy=list(map(int,input().split()))
xy=[]
for i in range(1,100):
    if xx%i==0 and yy%i==0:
        xy.append(i)
print(max(xy))
