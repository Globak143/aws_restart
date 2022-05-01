mystring = "This is my string."
print(mystring)
print(type(mystring))
print(mystring + " is of the data type" + str(type(mystring)))
firststing = "water"
secondstring = "fall"
thirdstring = firststing + secondstring
print(thirdstring)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{} , you like a {} {} !".format(name,color,animal))