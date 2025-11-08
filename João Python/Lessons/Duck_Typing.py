#Duck Typing = Another way to achieve polymorphism besides inheritance
#Name comes from the expression: "If it looks like a duck, and quacks like a duck, it must be a duck"

class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("WOOF WOOF!")

class cat(animal):
    def speak(Self):
        print("Meow...")

class car:
    def speak(self):
        print("HONK!")

animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    try:
        print(animal.alive)
    except AttributeError:
        print("False")

#The car object "quacks like a duck, so it must be a duck", but it isn't alive, so it isn't "a duck"