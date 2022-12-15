# Easier to run the python commands via the command line,
# ensure you are in the location the .txt file is
file = open("fruit.txt", "r")
# Reads the first line of a file
line = file.readline()
# Prints out the first line of the file
# print(line)
# Will close the most recently opened file
file.close()

file2 = open("fruit.txt", "r")
lines = file2.readlines()
# print(lines)
# for line in lines:
#     print(line)

fruitdb = open("fruitdb.txt", "r")
header = fruitdb.readline()
content = fruitdb.readlines()

# print(header)
print(content)
fruitHeaders = header.split(",")
fruitContent = []

for entry in content:
    splitEntry = entry.split(",")
    fruitContent.append(splitEntry)
print(fruitHeaders)
print(fruitContent)

fruitdb.close()

# Writing files
# When this file runs it will remove the content in this file, to append to the file use "a"
file = open("emptyFile.txt", "w")

for x in range(10):
    newLine = f"Line number {str(x + 1)} \n"
    file.write(newLine)

file.close

# Appending files
file = open("emptyfile.txt", "a")
file.write("New line!!!2")
file.close()

# With command lets you access files directly and run commands in that specific file
# Python will automatically close the file after and an exception won't crash the entire program
with open("fruit.txt", "r") as file:
    for line in file:
        print(line)


