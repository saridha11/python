def Single( ar, n):
    count=5
    res = ar[0] 
    for i in range(1,n): 
        res = res ^ ar[i] 
    return res
ar = [1,2,1,3,2] 
print ("Element occuring once is",Single(ar, len(ar)))
Single()
