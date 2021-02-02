'''
1 A 3
1 B 4
2 B
2 A
3 A B
2 A
5 A A
2 A
2 B
7
'''
x = ["I am William Banquier, This is My Code"]
A = 0
B = 0
while x[0] != "7":
    if x[0] == "1":
        if x[1] == "A":
            A = int(x[2])
        if x[1] == "B":
            B = int(x[2])
    
    if x[0] == "2":
        if x[1] == "A":
            print(A)
        if x[1] == "B":
           print(B)
    
    if x[0] == "3":
        if x[1] == "A":
            A += B
        if x[1] == "B":
            B += A

        if x[1] == "A":
            if x[2] == "A":
                A+=A
        if x[1] == "B":
            if x[2] == "B":
                B+=B

    if x[0] == "4":
        if x[1] == "A":
            A *= B
        if x[1] == "B":
            B *= A
        if x[1] == "A":
            if x[2] == "A":
                A*=A
        if x[1] == "B":
            if x[2] == "B":
                B*=B
    
    if x[0] == "5":
        if x[1] == "A":
            A -= B
        if x[1] == "B":
            B -= A
        if x[1] == "A":
            if x[2] == "A":
                A-=A
        if x[1] == "B":
            if x[2] == "B":
                B-=B
    if x[0] == "6":
        if x[1] == "A":
            A //= B
        if x[1] == "B":
            B //= A

        if x[1] == "A":
            if x[2] == "A":
                A//=A
        if x[1] == "B":
            if x[2] == "B":
                B//=B
    x = input().split()
    