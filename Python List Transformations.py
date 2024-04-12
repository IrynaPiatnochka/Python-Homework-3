#List of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Sorting the grades in descending order and displaying the sorted list

grades.sort(reverse=True)
print(grades)

#Calculating the average grade and displaying it

total = sum(grades)
average_grade = total/len(grades)
print(average_grade)

#Replacing any grade below 80 with the value Failed
# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# if grades < 80: print("Failed")

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "Failed"
grades[4] = "Failed"
grades[8] = "Failed"
print(grades)