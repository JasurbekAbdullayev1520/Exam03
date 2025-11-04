class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Ismi: {self.name}, yoshi {self.age} da"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  
        self.grade = grade           
    
    def introduce(self):
       
        return f"Ismi: {self.name}, yoshi {self.age} da ,{self.grade} da o'qiydi"


person1 = Person("Qodir", 30)
student1 = Student("Akbar", 16, "Samisi")


print(person1.introduce())  
print(student1.introduce())