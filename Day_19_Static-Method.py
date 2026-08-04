# Static method--> A method that belong to a class rather than
#                  any object from  class (instance) ususally used
#                  for general utility functions

# Instance method--> Best for operations on instance of the class(objects)
# Static method --> Best for utility function that do not need access to class data

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    # Instance methond::
    def get_info(self):
        return f"{self.name} = {self.position}"

    #Static method:
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions
     # when we use static method we no need to create object like employee1=Employee()


employee1 = Employee("Jose","Manager")
employee2 = Employee("Perez","Cashier")
employee3 = Employee("Pinto","Janitor")
employee4 = Employee("Brahim","Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())

print()
print(Employee.is_valid_position("Cook"))      # Static method 