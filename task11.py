class Vehicle:
    def __init__(self, brend, model):
        self.brend = brend
        self.model = model

    def move(self):
        return f"{self.brend} konpaniyasining {self.model} avtomobili harakatlanmoqda"

class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving"

v1 = Vehicle("Honda", "SuperBike")
print(v1.move())

c1 = Car("Chevrolet", "Malibu")
print(c1.move())
