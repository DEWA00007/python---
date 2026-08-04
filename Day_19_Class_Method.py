# Class Method:
# --> Allows operations related to the class itself
#      Take(cls) as the first parameter, which reperesent the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} : {self.gpa}"


    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total no.of students {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f" Avg GPA is: {cls.total_gpa/cls.count:.2f}"


student_1 = Student("Tom" ,3.5)
student_2 = Student("Andrew",3.68)
student_3 = Student("Tobby",3.75)

print(student_1.get_info())
print(student_2.get_info())
print(student_3.get_info())


print(Student.get_count())    
print(Student.get_avg_gpa())