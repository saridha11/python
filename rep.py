def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i])
    return repeated
list1 = [1,2,3,2,3,4,3]
print (Repeat(list1))
Repeat(x)
