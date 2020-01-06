def distSq( p,  q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])


def isSquare(p1, p2, p3, p4) :
    d2 = distSq(p1, p2)  
    d3 = distSq(p1, p3)  
    d4 = distSq(p1, p4)  

    if (d2 == d3 and 2 * d2 == d4 and 2 * distSq(p2, p4) == distSq(p2, p3)):
        return True

    if (d3 == d4 and 2 * d3 == d2 and 2 * distSq(p3, p2) == distSq(p3, p4)):
        return True

    if (d2 == d4 and 2 * d2 == d3 and 2 * distSq(p2, p3) == distSq(p2, p4)):
        return True

    return False
a,b = [int(x) for x in input().split()]
p1 = [a,b]
a,b = [int(x) for x in input().split()]
p2 = [a,b]
a,b = [int(x) for x in input().split()]
p3 = [a,b]
a,b = [int(x) for x in input().split()]
p4 = [a,b]

if isSquare(p1, p2, p3, p4):
    print("yes")
else:
    print("no")
