a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
count=0
for i in range(0,len(c)-1):
    for sec in range(i+1,len(c)-1):
        if(c[i]+c[sec]==b):
            count+=1
if (count==1):
    print("yes")
else:
    print("no")
