count=input()
a=list(map(int,input().split()))
min=999
for i in a:
  if i <min:
    min=i
print(min)
