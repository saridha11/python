def square(a, b, c, d):  
    if a == b == c == d: 
        return True
          
    elif a == b and c == d: 
        return True
          
    elif a == d and c == b: 
        return True
          
    elif a == c and d == b: 
        return True
          
    return False
a,b,c,d=map(int,input().split())
print("Yes" if square(a, b, c, d) else "No")
square(a, b, c, d)
  
