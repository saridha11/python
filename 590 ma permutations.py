from itertools import permutations
s = input()
L = [ ''.join(x) for x in list(permutations(s,len(s)))]
L2 = list(set(L))
#print(L2)
sum1=0
for x in L2 :
    sum1 += int(x)
print(sum1)
