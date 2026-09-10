# File in python (Student details)

name = input("Enter student name: ")
age = input("Enter age: ")
roll_no = input("Enter roll number: ")
course = input("Enter course: ")
marks = input("Enter marks: ")
with open("student.txt", "w") as file:
    file.write("Student Details\n")
    file.write("----------------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Roll No: {roll_no}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

print("\nStudent details saved successfully!")

with open("student.txt", "r") as file:
    details = file.read()

print("\nSaved Student Details:")
print(details)
