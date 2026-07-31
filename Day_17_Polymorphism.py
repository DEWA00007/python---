# Polymorphism --> means same name with many forms
 #               Two ways to achieve this ::>
#                1. Inheritance 
#                2."Duck typing"--> object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area (self):
        pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass

"""circle = Circle()  # circle has Circle and Shape attributes not Square and Triangle
square = Square()  # square has Square and Shape not circle and triangle
"""

shapes = [Circle(),Square(),Triangle()]
                                       