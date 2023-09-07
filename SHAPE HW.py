class Shape:
 def __init__(self):
  return

class Circle(Shape):
 def __init__(self, radius):
  super().__init__()
  self.radius = radius
 def calculate_perimeter(self,):
  pi=3.14
  return 2 * pi * self.radius
 def calculate_area(self):
 pi=3.14
 return pi * self.radius ** 2
  pi=3.14
  return pi * self.radius**2

class Triangle(Shape):
 def __init__(self, base, height):
  super().__init__()
  self.base = base
  self.height = height

def calculate_perimeter(self):
 return self.base + (2 * ((self.height ** 2) + (self.base ** 2)) ** 0.5)
def calculate_area(self):
 return (self.base * self.height) / 2

class Rectangle(Shape):
 def __init__(self, length, width):
  super().__init__()
  self.length = length
  self.width = width
  
def calculate_perimeter(self):
 return 2 * (self.length + self.width)

def calculate_area(self):
 return self.length * self.width

circle = Circle(6)
triangle = Triangle( 6, 2)
rectangle = Rectangle( 3 ,2 )
print("area of circle")
print(Circle.calculate_area())
print("preimeter of circle")
print(circle.calculate_perimeter())

print("area of triangle")
print(triangle.calculate_area())
print("perimeter of triangle")
print(triangle.calculate_perimeter())

print("area of rectangle")
print(rectangle.calculate_area())
print("perimeter of rectangle")
print(rectangle.calculate_perimeter())

