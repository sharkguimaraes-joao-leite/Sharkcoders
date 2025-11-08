#Polymorphism = Greek word that means to "Havee many forms or faces"
from abc import ABC, abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class triangle(shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.base * self.height * 0.5
    
class pizza(circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [circle(5), square(4), triangle(3, 5), pizza("pepperoni", 6)]

for shape in shapes:
    print(f"The area is {shape.area()} cm^2")

#Pizza is a circle and a shape, and triangles, squares and circles are shapes but not pizzas (duh...)