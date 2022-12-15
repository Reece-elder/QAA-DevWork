# Part 1 

# # Task 1
# ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
# print(ages)

# length = len(ages)
# print(length)

# for age in ages:
#     print(age)

# for age in ages:
#     count = 0
#     ages[count] = ages[count] + 1
#     count += 1

# count = 0
# while count < len(ages):
#     if ages[count] <= 16 or ages[count] >= 65:
#          del ages[count]
#          count -= 1
#     count += 1
# print("---------------------------")
# print(len(ages))
# print(ages)

# ageCount = 0
# for age in ages:
#     if age >= 16 and age <= 25:
#         ageCount += 1

# print(ageCount)

# ages.sort()
# print(ages)

# print(f"Number of users between 16 - 25: {ageCount}, this is {ageCount / len(ages) * 100}%")

# Part 2
inputString = input("Please enter a string: ")

count = 0
for char in inputString:
    if char in ("a", "e", "i", "o", "u"):
        count += 1
print(f"Number of vowels in {inputString} is {count}")


