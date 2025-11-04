class Rectangle:
    def __init__(self, width, height ,  ):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

a = Rectangle(5, 10)
b = Rectangle(3, 4)
print("Yuzi:", a.area())
print("Perimeter:", b.perimeter())