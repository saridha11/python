a=int(input())
b=list(map(int,input().split()))
xy=[1]*a
for i in range(a):
    if(i==0):
        if b[i]>b[i+1]:
            xy[i]=xy[i]+xy[i+1]
    else:
        if b[i]>b[i-1]:
            xy[i]=xy[i]+xy[i-1]
print(sum(xy))
