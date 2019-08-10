a,b=map(int,input().split())
c=[str(i) for i in input().split()]
d=[]
e=0
f=" "
if len(c)==1:
    f=c
else:
    for i in range(len(c)-b,len(c)):
        if len(c)<b:
            d.append(c[i])
            e=1
        else:
            d.append(c[i])
    if e==1:
        d=dict.fromkeys(d)
    for i in range(0,len(c)-b):
        d.append(c[i])
    for i in d:
        print(i,end=" ")
    for i in f:
        print(i)
