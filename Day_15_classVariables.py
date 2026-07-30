# Class variables---> shared among all instance of a class
#                     Defined outside the constructor
#                     Allow you to share data among all objects created from that class

class Student:

    class_year = 2000     # class variable .
    num_stu = 0


    def __init__(self,name,age):     
        self.name = name           # instance variable
        self.age = age 
        Student.num_stu += 1    

student1 = Student("Harry",34)
student2 = Student("Ramos",39)        
student3 = Student("Silva",46)        

print(student2.name)
print(student2.age)
print(Student.class_year)
print()

# Print how many students are there;;
print( Student.num_stu )
