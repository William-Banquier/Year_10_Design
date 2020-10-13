try:
    import math

   

    number1 = int (input ("Enter an Interger: "))
    number2 = int (input ("Enter an Interger: "))



    answer = number1 * number2
    print (answer)

    answer = number1 / number2
    print (answer)
    print (math.floor (answer))
    print (math.ceil (answer))
    print (math.trunc (answer))

    answer = number1 // number2
    print (answer)

    answer = number1 % number2
    print (answer)

    if number1 % number2 == 0:
        print (number1, "is a multiple of", number2)

    elif number2 % number1 == 0:
        print (number1, "is a multiple of", number2)

    else:
        print (number1, "is not a multiple of", number2)




except:
    print("You have found an error, error message has been sent. Our team of developers are fixing your error")


counter = 0
while  counter < 10:
    print (counter)
    counter += 2

print("\n"*2)
for counter in range (10, 0, -1):
    print (counter)


numbers = [i + 1 for i in range(100)]


for i in numbers:
    print(i, end = " ")