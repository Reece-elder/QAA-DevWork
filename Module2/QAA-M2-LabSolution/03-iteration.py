# Part 1 Using while loops

# Task 1 - Squares
number = 1
while number < 100:
    print(f"Number: {number}")
    print(f"Square of number: {number**2}")
    if number**2 > 2000:
        break
    number += 1

# Task 2 - Factorial

number = int(input("Please enter an integer: "))
count = 1
factorial = 1
while count <= number:
    factorial = factorial * count
    count += 1

print(f"factorial of {number} is {factorial}")

# Task 3 - Investment
initial = 100
goal = 1000
interest = 10
month = 0

while initial < goal:
    initial = initial + (initial * (interest / 100))
    month += 1

print(f"Took {month} months to reach {goal} starting with {initial}")

initialInput = int(input("Please enter starting value: "))
goalInput = int(input("Please enter goal value: "))
interestInput = int(input("Please enter interest value as an integer (10% = 10 e.g): "))

while initialInput < goalInput:
    initialInput = initialInput + (initialInput * (interestInput / 100))
    month += 1

print(f"Took {month} months to reach {goalInput} starting with {initialInput}")

# Task 4 
min = 5
max = 100
tries = 0
correct = False

while tries < 3: 
    guess = int(input(f"Please enter a number to guess the range of values: "))
    if guess >= min or guess <= max:
        correct = True
        break
    else: 
        print("Incorrect! try again!")
        tries += 1
     
if correct:
    print("Nice, you guessed right!")
else: 
    print(f"Sorry.. you guessed wrong.. it was between {min} and {max}")

# Task 5 Count Vowels
inputString = input("Please enter a string: ")

count = 0
for char in inputString:
    if char in ("a", "e", "i", "o", "u"):
        count += 1
print(f"Number of vowels in {inputString} is {count}")

# Task 5 - Exam average

grade1 = int(input("Please enter a value between 1 and 100: "))
grade2 = int(input("Please enter a value between 1 and 100: "))
grade3 = int(input("Please enter a value between 1 and 100: "))

averageGrade = (grade1 + grade2 + grade3) / 3

if averageGrade >= 65:
    print("Pass!")
else:
    print("Fail :(")

maths = 0
english = 0
it = 0

while maths == 0:
    inputGrade = int(input("Please enter a value between 1 and 100: "))
    if inputGrade < 1 or inputGrade > 100:
        print("Not a valid grade, try again")
    else:
        maths = inputGrade

while english == 0:
    inputGrade = int(input("Please enter a value between 1 and 100: "))
    if inputGrade < 1 or inputGrade > 100:
        print("Not a valid grade, try again")
    else:
        english = inputGrade
        
while it == 0:
    inputGrade = int(input("Please enter a value between 1 and 100: "))
    if inputGrade < 1 or inputGrade > 100:
        print("Not a valid grade, try again")
    else:
        it = inputGrade

averageGrade2 = (maths + english + it) / 3
print(f"Average grade is {averageGrade2}: maths = {maths}, english = {english}, it = {it}")

# Part 2
# Task 1 - Squares
for number in range(101):
    print(f"Number: {number}")
    print(f"Square of number: {number**2}")
    if number**2 > 2000:
        break
    number += 1

# Task 2 Factorial
startValue = int(input("Please enter an integer: "))
result = 1

for value in range(1, startValue + 1):
    result = result * value

print(f"Factorial of {startValue} is {result}")

for number in range(20, 0, -2):
    print(number)

