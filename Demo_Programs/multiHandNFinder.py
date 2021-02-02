n = int(input())



def findN(n):
    c = 0
    allCounts = []
    for leftHandFingers in range(0,6):
        for rightHandFingers in range(0,6):
            if leftHandFingers + rightHandFingers == n:
                c+=1
                if leftHandFingers == rightHandFingers:
                    return c
                
    return int(c/2)
print(findN(n))