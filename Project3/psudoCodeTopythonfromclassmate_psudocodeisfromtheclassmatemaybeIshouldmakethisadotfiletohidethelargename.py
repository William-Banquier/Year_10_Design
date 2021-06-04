
def fractionCode(): #Made this a function so that the return statement would not break the code
    class fraction(): #Added class fraction so that I could make a custon fraction type to not cause an error below
        def __init__(self,value):
            value = list(map(float, value.split("/"))) #Made as list of floats so that is_integer() works
            self.neumerator = value[0]
            self.denominator = value[1]

    fraction = fraction(input()) #Fraction is around input as below it is defined as a class
    Modulus = -1 #This has to be defined, -1 is a value that it can never naturally be.
    if fraction.neumerator >= 0 and fraction.denominator >= 1:
        if fraction.neumerator.is_integer() and fraction.denominator.is_integer():
            Modulus = int(fraction.neumerator) % int(fraction.denominator)
        if Modulus != 0:
            return Modulus 
            Output = "fraction.neumerator / fraction.denominator" + Modulus 
print(fractionCode()) #Print is just there if you want to view the output from the function