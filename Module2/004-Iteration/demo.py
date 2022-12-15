# Iteration - repeating a block of code for ease of development

# While Iteration
counter = 1
while counter < 10:
    print("Value of counter: " + str(counter))
    counter += 1

# Break - Breaks out of an interation loop when the break command is run
counter = 1
while counter < 10:
    print("Value of counter: " + str(counter))
    counter += 1

    if counter == 6:
        break

# Range - Produces a range of values based on the variables passed in
print(range(5)) # Doesn't show all values
print(*range(5)) # Shows values on single line
print(*range(4,8)) 
print(*range(10,0,-2)) 

# Range useful for iteration loops! 
for x in range(10):
    print("Value of x: " + str(x))

for x in range(20, 3, -3):
    print("Value of x: " + str(x))



