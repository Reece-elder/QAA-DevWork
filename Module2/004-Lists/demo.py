# Arrays (briefly covered before) are ways of storing a sequence of like data
# Four different groups of arrays

# Lists - ordered, mutable, collection of values (Standard)
# Tuples - ordered, immutable, collection of values 
# Dictionaries - unordered, mutable, collection of key-value pairs
# Sets - unordered, mutable, collection of unique values

# Lists
shapes = ["square", "triangle", "circle", "pentagon"]
# Access the values by indexing
print(shapes[2])
# Loop backwards through the index with negative values 
print(shapes[-1])
# Slice an array
print(shapes[1:3])
# Modifying a value
shapes[1] = "rhombus"
print(shapes[1])
# Check memberships
print("circle" in shapes)

# Lists can contain any types of data
cafe_order = [12, ["latte", "carrot cake"], True]
print(cafe_order)
print(cafe_order[1])
print(cafe_order[1][0])

# Access the length of an array with len
print(len(shapes))

# Adding a value to the end
shapes.append("star")
shapes.remove("star")

## Tuples - Cannot be modified once declared
new_tuple = ("This", "list", "can't", "change", ":(")
print(new_tuple[1])
# new_tuple[2] = "Hello"

## Dictionaries - Key Value pairs similar to a list
noises = {"cow" : "moo!", "duck" : "quack!" }
noises["Chicken"] = "cluck!"
noises["Number"] = 123
print(noises)

## Sets - Unordered mutable set of unique values
fruit_set = {"Apple", "Banana", "Apple", "Banana", "Orange"}
print(fruit_set)


# Loops useful for arrays 
colours = ["Maroon", "Teal", "Fuschia"]
for x in colours:
    print(x)

# Nested Loops, loops within loops
letters = ["A", "B", "C", "D"]

# for x in letters:
#     for y in range(1, 5):
#         print(x + str(y))