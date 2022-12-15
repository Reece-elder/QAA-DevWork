# Part 1 
age = int(input("Please enter age: "))

if age >= 18:
    print("You are in Cat A")
elif age >= 16:
    print("You are in Cat B")
else:
    print("You are in Cat C")

# Part 2
# Task 1 
num1 = int(input("Please enter num1: "))
num2 = int(input("Please enter num2: "))

print("1. Add +\n2. Subtract -\n3.Multiply *\n4. Divide / \n5. Power p")
calculation = input("Please choose operation (+, -): ")
if calculation == "+":
    print(num1 + num2)
elif calculation == "-":
    print(num1 - num2)
elif calculation == "*":
    print(num1 * num2)
elif calculation == "/":
    print(num1 / num2)
elif calculation == "p":
    print(num1**num2)
else:
    print("Wrong symbol!")

# Task 2 
examGrade = int(input("Please enter a grade between 1 and 100"))
if examGrade < 1 or examGrade > 100:
    print("Error: marks must be between 1 and 100")
elif examGrade < 50:
    print("Fail :(")
elif examGrade <= 60:
    print ("Pass :)")
elif examGrade <= 70:
    print("Merit :D")
else:
    print("Distinction! :D :D")

# Task 3
examGradeTask3 = int(input("Please enter a grade between 1 and 100"))
if examGradeTask3 < 1 or examGradeTask3 > 100:
    print("Error: marks must be between 1 and 100")
examLevel = int(input("Please enter level (either 1 or 2): "))
if examLevel == 1:
    if examGrade < 50:
        print("Fail :(")
    elif examGrade <= 60:
        print ("Pass :)")
    elif examGrade <= 70:
        print("Merit :D")
    else:
        print("Distinction! :D :D")
elif examLevel == 2:
    if examGrade < 40:
        print("Fail :(")
    elif examGrade <= 50:
        print ("Pass :)")
    elif examGrade <= 65:
        print("Merit :D")
    else:
        print("Distinction! :D :D")
else: 
    print("Exam level isn't valid..")

Task 4
from math import sqrt
print("""
Pythagoras' Calculator  
1.	Find the length of A given B and C  
2.	Find the length of B given A and C 
3.	Find the length of C given A and B 
""")

task4_choice = int(input("Please enter choice (1,2,3): "))

if task4_choice == 1:
    b_length = int(input("Please enter value for length B: "))
    c_length = int(input("Please enter value for length C: "))
    a_length = (c_length ** 2) - (b_length ** 2)
    a_length = sqrt(a_length)
    print(a_length)
elif task4_choice == 2:
    a_length = int(input("Please enter value for length A: "))
    c_length = int(input("Please enter value for length C: "))
    b_length = (c_length ** 2) - (a_length ** 2)
    b_length = sqrt(b_length)
    print(b_length)
elif task4_choice == 3:
    a_length = int(input("Please enter value for length A: "))
    b_length = int(input("Please enter value for length b: "))
    c_length = (b_length ** 2) + (a_length ** 2)
    c_length = sqrt(c_length)
    print(c_length)
