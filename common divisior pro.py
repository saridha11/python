def isCommonBase(base, s1, s2): 
    for j in range(len(s1)):  
        if (base[j % len(base)] != s1[j]): 
            return False 
    for j in range(len(s2)):  
        if (base[j % len( base)] != s2[j]): 
            return False
  
    return True
  
def countCommonBases(s1, s2):  
    n1 = len(s1) 
    n2 = len(s2) 
    count = 0
    for i in range(1, min(n1, n2) + 1): 
        base = s1[0: i] 
        if (isCommonBase(base, s1, s2)): 
            count += 1
          
    return count 
if __name__ == "__main__": 
      
    s1 = input()
    s2 = input()
    print(countCommonBases(s1, s2)) 
  
