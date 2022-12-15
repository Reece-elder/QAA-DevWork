data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")

gradesInt = []
for x in grades:
    gradesInt.append(int(x))

print(min(gradesInt))

print(max(gradesInt))

# Mapping 
gradeMap = list(map(int, grades))
print(gradeMap)

averageGrade = sum(gradesInt) / len(gradesInt)
print(averageGrade)
print(round(averageGrade, 2))

import statistics

averageGradeQuick = statistics.mean(gradesInt)
print(averageGradeQuick)

medianGrade = statistics.median(gradesInt)
print(medianGrade)