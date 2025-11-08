#P.O.O.P = Python Object Oriented Program

#Object = A "bundle" of related atributes (variables) and methods (functions)
#         You need a "class" to create many objects

#Class = Blueprint used to desing the structure and layout of an object

class phone:
    def __init__(self, version, is_on, is_online, battery):
        self.version = version
        self.is_on = is_on
        self.is_online = is_online
        self.battery = battery

#To create classes with methods, always use def __init__(self) and then add other values

phone1 = phone("Iphone 17", True, False, 75)
phone2 = phone("Samsung", False, False, 83)
phone3 = phone("Galaxy 17 5G", True, True, 64)

print("1st phone:")
print("************")
print(phone1.version)
print(phone1.is_on)
print(phone1.is_online)
print(f"{phone1.battery}%")
print("************")
print("-------------------------")
print("2nd phone:")
print("************")
print(phone2.version)
print(phone2.is_on)
print(phone2.is_online)
print(f"{phone2.battery}%")
print("************")
print("-------------------------")
print("3rd phone:")
print("************")
print(phone3.version)
print(phone3.is_on)
print(phone3.is_online)
print(f"{phone3.battery}%")
print("************")

#-------------------------------------------------------------------

class car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    def drive(self, km):
        print(f"You are driving your {self.color} {self.model} at {km} per hour.")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}.")

car1 = car("Mustang", "yellow", 2017, False)

car1.drive(36)
print("-------------------------")
car1.stop()
print("----------------------------------------------------------------")

#Class Variables = Variables shared among all instances of a class

class student:

    grad_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Afonso", 13)
student2 = student("Luis", 9)
student3 = student("Gonçalo", 15)

print(f"{student1.name} is {student1.age} years old and is going to graduate in {student.grad_year}.")
print("-------------------------")
print(f"With them, we have {student.num_students} students in their class!")
print("-------------------------")