#Lists of students, grades and activities

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance" ]

#Name, grade and activiy of students with a score below 80

print(students[2], grades[2], activities[2])

#Creating new list "students_approved"

students_approved = students.copy()
students_approved.remove("Jane")
print(students_approved)