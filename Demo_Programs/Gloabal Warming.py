'''
7 3 4 6 4 5 7 5 
3 1 3 5 
3 1 4 5 
4 3 4 6 7
0
'''

line = "7 3 4 6 4 5 7 5 ".split()
x = []
for i in range(len(line)):
    try:
        x.append(abs (int (line [i]) - int (line [i+1])))
    except:
        pass
print(x)