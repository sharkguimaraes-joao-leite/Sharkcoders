#Inheritance = Allows a class to inherit atributes and methods from another class

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is asleep...")

class dog(animal):
    def talk(self):
        print("WOOF WOOF!")

class cat(animal):
    def talk(self):
        print("Meow...")

class mouse(animal):
    def talk(self):
        print("Squeak!")

dog1 = dog("Link")
cat1 = cat("Zelda")
mouse1 = mouse("Ganon")

dog1.eat()
dog1.talk()
print("-------------------------")
cat1.sleep()
cat1.talk()
print("-------------------------")
mouse1.eat()
mouse1.talk()
print("---------------------------------------------------------")

#Multiple Inheritance = Inherit more than one class

class prey:
    def __init__(self, species):
        self.species = species

    def flee(self):
        print(f"This {self.species} is fleeing!")

class predator:
    def __init__(self, species):
        self.species = species

    def hunt(self):
        print(f"This {self.species} is hunting for prey!")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey, predator):
    pass

rabbit1 = rabbit("rabbit")
hawk1 = hawk("hawk")
fish1 = fish("fish")

rabbit1.flee()
print("-------------------------")
hawk1.hunt()
print("-------------------------")
fish1.flee()
print("-------------------------")
fish1.hunt()
print("------------------------------------------------------------------")

#Multi-level Inheritance = A class inherits from a class that inherrits from another class and so on
class animal:
    def __init__(self, species):
        self.species = species
    
    def eat(self):
        print(f"This {self.species} is eating its meal")

    def sleep(self):
        print(f"This {self.species} is sleeping...")

class prey(animal):
    def flee(self):
        print(f"This {self.species} is fleeing!")

class predator(animal):
    def hunt(self):
        print(f"This {self.species} is hunting for prey!")

class mouse(prey):
    pass

class lion(predator):
    pass

class chicken(prey, predator):
    pass

class gorilla(predator):
    pass

mouse1 = mouse("mouse")
lion1 = lion("lion")
chicken1 = chicken("chicken")
gorilla1 = gorilla("gorilla")

mouse1.flee()
print("-------------------------")
lion1.sleep()
print("-------------------------")
chicken1.hunt()
print("-------------------------")
gorilla1.eat()
print("---------------------------------------------------------------------------")

#Super Method = Function used in a child class to call methods from a parent class

class shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class circle(shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class square(shape):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side

class triangle(shape):
    def __init__(self, color, filled, height, width):
        super().__init__(color, filled)
        self.radius = height
        self.width = width

circle1 = circle("Red", True, 5)
square1 = square("Blue", False, 3)
triangle1 = triangle("Green", True, 5, 4)

print(circle1.color)
print(triangle1.width)
print(square1.side)