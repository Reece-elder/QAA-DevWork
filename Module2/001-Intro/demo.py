# Comments are made with '#'

# Print out to the console with print('text')
print('Hellooo')

# To see our app doing 'something' we need to start the .py file
# Visual Studio reads everything from startup file, top to bottom
print('Now me!')

# Python has three basic data types
# Number
tiers = 2
price = 8.99
# String
flavour = "Black Forest"
# Boolean (True or False CASE SENSITIVE)
decorated = True
# Arrays (collection of any data types)
favFruits = ["Mango", "Kiwi", "Banana"]
print(favFruits)
print(favFruits[1])

# Python bad naming conventions
#percentage% = 30
#customer-name = "Aubrey"
#last name = "Milana"
#print = "Photo of family"
#Email = "email@admin.com"

# Inputs allow us to enter values (and save them as variables)
fav_colour = input('Please enter your fav colour: ')
print(fav_colour)

# String concatenation (adding strings together)
username = input('Please enter username: ')
print(username + " succesfully logged in")

# Cannot add numbers and strings
# Input is ALWAYS string (unless casting)
savings = input('Please enter savings: ')
# savings = savings + 100

# Casting - Converting data types 
fav_number = int(input('What is your fav number? '))
my_fav_number = fav_number + 1
print('Well.. mine is ' + my_fav_number + ' which is better')

sum = 5 + 4
print("Sum is " + str(sum))