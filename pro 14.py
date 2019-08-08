r,p=map(int,input().split())
m=list(map(int,input().split()))
q=[]
for i in range(0,p):
    d = []
    d=list(map(int,input().split()))
    s = m[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^m[j]
    q.append(s)
for i in range(0,len(q)):
    print(q[i]) 
