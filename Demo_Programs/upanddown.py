a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = int(input())

nickyCount = 0
bryonCount = 0

# if a+b % s == 0:
#     print(a+b)
def runB(a,b,s,bryonCount):
    if (12 % (a+b)) == 0:
        bryonCount = int((12/(a+b)) * (a - b))
        return bryonCount
    if s / (a+b) > 1:
        print("True")


def runN(c,d,s,nickyCount):
    if (12 % (c+d)) == 0:
        nickyCount = int((12/(c+d)) * (c - d))
        return nickyCount
    if s / (c+d) <= 1:
        return c-d
        


bryonCount = (runB(a,b,s,bryonCount))
nickeyCount = runN(c,d,s,nickyCount)
print("Bryon Count is equal to" ,bryonCount)
print("Nicky Count is equal to" ,nickyCount)