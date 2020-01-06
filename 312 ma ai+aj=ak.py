n=int(input())
l=list(map(int, input().split())) 
c=0
for I in range(0,len(l) -2):
  for j in range(I+1, len(l) -1) :
    for k in range(j+1, len(l)) :
      if(l[I]+l[j]==l[k]) :
        c=c+1 
print(c) 
