def change(s1, s2): 
    l = len(s1) 
    r = len(s2) 
    if abs(l - r) > 1: 
        return false
    count = 0
    i = 0
    j = 0
    while i < l and j < r: 
        if s1[i] != s2[j]: 
            if count == 1: 
                return false 
            if l > r: 
                i+=1
            elif l < r: 
                j+=1
            else:    
                i+=1
                j+=1
            count+=1
  
        else:    
            i+=1
            j+=1
    if i < l or j < r: 
        count+=1
  
    return count == 1
s1 = "aab"
s2 = "aay"
if change(s1, s2): 
    print ("yes")
else: 
    print ("no")
change(s1,s2)
