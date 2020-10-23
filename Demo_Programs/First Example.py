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

#Unhide later
# for i in numbers:
#     print(i, end = " ")



import os 
os.system("clear")

import json

jString = '{"name":"Felix","age":20,"city":"Toronto"}'
data = json.loads(jString)

print(data["city"])

jString = '{"name":{"firstName":"Cleopatra", "lastName":"Ptolemy"}, "address":{"city":"Alexandria", "province":"Egypt"}}'
data = json.loads(jString)


print(data["name"]["firstName"])

jString = '[{"name":{"firstName":"Cleopatra", "lastName" : "Ptolemy"}, "address": {"city":"Alexandria", "province":"Egypt"}}, {"name":{"firstName":"Marc", "lastName":"Antony"}, "address":{"city":"Rome", "province":"Italia"}}]'
data = json.loads(jString)

print(data[1]["address"]["city"])

#JSON import is not needed for this... thats okay
x = [{"name":{"firstName":"Cleopatra", "lastName" : "Ptolemy"}, "address": {"city":"Alexandria", "province":"Egypt"}}, {"name":{"firstName":"Marc", "lastName":"Antony"}, "address":{"city":"Rome", "province":"Italia"}}]
print(x[1]["address"]["city"])



inData = '{"quiz": {"sport": {"q1": {"question": "Which one is a correct team name in NBA?","options": ["New York Bulls","Los Angeles Kings","Golden State Warriros","Houston Rocket"],"answer": "Houston Rocket"}},"maths": {"q1": {"question": "5 + 7 = ?","options": ["10","11","12","13"],"answer": "12"},"q2": {"question": "12 - 8 = ?","options": ["1","2","3","4"],"answer": "4"}}}}'

jsonFormat = json.loads(inData)

print (jsonFormat['quiz']['sport']['q1'])
info = list(jsonFormat["quiz"])

for i in range(len(info)):
    print("Topic",str(i+1)+".",list(info)[i].capitalize())