count=input()
a=list(map(int,input().split()))
for item in a:
  print(a.index(item)+1,item)
