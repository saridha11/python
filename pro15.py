l=int(input())
m=list(map(int,input().split()))[0:l]
m.sort(reverse=True)
i=0
while i<l:
    print(m[i],end="\n")
    i+=1
