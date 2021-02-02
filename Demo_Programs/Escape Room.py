M = int(input())
N = int(input())


def check():
    for c in range(M):
        for r in range(N):
            t = c*r
            try:
                if area[x][y] == t:
                    print("True", (area[x][y]), t)
            except:
                pass
def ifEnterable(area, M, N):
    for y in range(len(area)):
        for x in range(len(area[y])):

            
            

                    


#location = r, c
r = 0
c = 0

area = []

for i in range(M):
    x = input().split()
    z = []
    for y in range(N):
        z.append(int(x[y]))
    area.append(z)
print(area)

ifEnterable(area, M, N)