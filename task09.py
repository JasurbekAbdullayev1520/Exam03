class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} -> {self.sound}")

dog = Animal("It", "vov")
cat = Animal("Mushik", "miyov")

dog.make_sound()
cat.make_sound()