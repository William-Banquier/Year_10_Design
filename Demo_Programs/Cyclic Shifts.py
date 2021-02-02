#Last year I could not complete this quickly, but now it is quick and finished
T = input("Input Text: ")
S = input("Input String: ")

def findAllShifts(S):
    allShifts = [S]
    for i in range(0,len(S)):
        allShifts.append(allShifts[i][1::] + allShifts[i][0])
    return allShifts
def findIfIn(T,S):
    for i in range(len(S)):
        if S[i] in T:
            return "yes"
    return "no"
print(findIfIn(T, findAllShifts(S)))