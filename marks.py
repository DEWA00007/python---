def calculate_grade(name, marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "name": name,
        "average": average,
        "grade": grade
    }


student = calculate_grade("Alan", [85, 92, 78, 90])

print(f"Name: {student['name']}")
print(f"Average: {student['average']:.1f}")
print(f"Grade: {student['grade']}")
