class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [
    Rectangle(5, 3),   
    Circle(4),         
    Rectangle(2, 6),    
    Circle(3)          
]
for i, shape in enumerate(shapes, 1):
    print(f"Shape {i} area: {shape.area()}")