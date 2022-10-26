# Selection / Conditionals
# If this is true.. do this
# Else.. do this

colour = "purple"

if colour == "purple":
    print("Colour is Purple! :) ")
else: 
    print("Colour is not purple :( ")

# else if
age = int(input('Please enter your age: '))

my_age = 26

if age < my_age: 
    print("You're younger than me!")
elif age == my_age:
    print("We're the same age!")
elif age > my_age: # How could this be more efficient??
    print("You're older than me!")

# Logical AND OR + nested elif
shape = "square"
solid = True

if(shape == "square" and solid == True):
    print("Shape is Square and Solid")
elif(shape != "square" and solid == True):
    print("Shape is not square and solid")
elif(shape == "square" and solid == False):
    print("Shape is square and not solid")
else:
    print("Shape is not square or solid")

if(shape == "square" or solid == True):
    if(shape != "square"):
        print("Shape is not Square and is Solid")
    elif(solid == False):
        print("Shape is Square and not Solid")
    else:
        print("Shape is Square and Solid")
else:
    print("Shape is not square or solid")


