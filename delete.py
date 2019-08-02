import math
def deleteFromStart(num, n): 
    d = (math.log10(num) + 1);
    rev_new_num = 0; 
    i = 0; 
    while (num != 0): 
        digit = num % 10; 
        num = int(num / 10); 
  
        if (i != (int(d) - n)): 
            rev_new_num = ((rev_new_num * 10) +
                                        digit); 
        i += 1; 
    new_num = 0; 
    i = 0; 
    while (rev_new_num != 0): 
  
        new_num = ((new_num * 10) + 
                   (rev_new_num % 10)); 
        rev_new_num = int(rev_new_num / 10); 
        i += 1; 
    return new_num; 
def deleteFromEnd(num, n): 
    rev_new_num = 0; 
    i = 1; 
    while (num != 0): 
  
        digit = num % 10; 
        num = int(num / 10); 
  
        if (i != n): 
            rev_new_num = ((rev_new_num * 10) +
                                        digit); 
        i += 1; 
    new_num = 0; 
    i = 0; 
    while (rev_new_num != 0): 
  
        new_num = ((new_num * 10) + 
                   (rev_new_num % 10)); 
        rev_new_num = int(rev_new_num / 10); 
        i += 1; 
    return new_num; 
num = 2131; 
print("Number:", num); 
n = 4; 
print("Digit to be deleted:", n); 
print("Number after", n,  
      "digit deleted from starting:",  
            deleteFromStart(num, n)); 
print("Number after", n,  
      "digit deleted from ending:",  
            deleteFromEnd(num, n));
deleteFromEnd(num,n)
deleteFromStart(num,n)
