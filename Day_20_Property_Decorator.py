# @property = Decorator used to define  a method as a property (it can be accessed like an attribute)
#             Benefits--> Add additional logic when read,write or delete attributes
#             Gives you getter ,setter and deleter method

class Rectangle:
    def __init__(self,width,height):
        self._width = width   # _width is the private modifier  only this class can access it
        self._height = height  # same private access modifier

    @property # getter method
    def width(self):
        return f"{self._width:.2f} cm"    

    @property
    def height(self):
            return f"{self._height:.2f} cm"  

    @width.setter # setter method
    def width(self,new_widht):
         if new_widht > 0:
              self._width = new_widht
         else:
              print("width must be greater than 0")

    @height.setter
    def height(self,new_height):
         if new_height >0:
              self._height= new_height
         else:
              print("Height must be greater than 0")     

 # deleter method
    @width.deleter
    def width(self):
         del self._width
         print("widht has been deleted")
                           

     
rectangle = Rectangle(3,5)
rectangle.width = 4 # this to change the value of width

"""del rectangle.width # this deleted the width""" 


print(rectangle.width)
print(rectangle.height)

    