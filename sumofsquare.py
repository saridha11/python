a=int(input())
sum=0
while(a>0):
    x=a%10
    sum=sum+x*x
    a=a//10
print(sum)
