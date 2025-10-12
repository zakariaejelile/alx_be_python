import math

# Base class
class Shape:
    def area(self):
        
       # This method should be overridden in derived classes.
    
        raise NotImplementedError("Subclasses must override area() method")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2