def calculate_average_grades():
    grades = []
    while True:
        grade = input("Enter a grade (-1 to stop): ")
        if grade == '-1':
            break
        grades.append(int(grade))
    average_grade = sum(grades) // len(grades)
    return average_grade, grades

# Calculate average grades
average, grades = calculate_average_grades()
print("Average Grade:", average)
print("Grades in order:")
for grade in grades:
    print(grade)