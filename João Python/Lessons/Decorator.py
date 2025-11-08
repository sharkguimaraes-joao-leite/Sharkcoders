#Decorator = A function that extends the behavior of another function
import time

def add_sprinkles(func):
    def sprink(*args, **kwargs):
        print("*You added sprinkles*")
        func(*args, **kwargs)
    return sprink

def add_cream(func):
    def cream(*args, **kwargs):
        print("*You added cream*")
        func(*args, **kwargs)
    return cream

while True:
    act1 = input("Do you want sprinles (y/n)?: ").lower()
    if act1 == "y" or act1 == "n":
        break
    else:
        print("Write y or n")

while True:
    act2 = input("Do you want cream (y/n)?: ").lower()
    if act2 == "y" or act2 == "n":
        break
    else:
        print("Write y or n")

if act1 == "y" and act2 == "n":
    @add_sprinkles
    def get_cupcake(flavor):
        print(f"Here is your {flavor} cupcake 🧁")
elif act1 == "n" and act2 == "y":
    @add_cream
    def get_cupcake(flavor):
        print(f"Here is your {flavor} cupcake 🧁")
elif act1 == "y" and act2 == "y":
    @add_cream
    @add_sprinkles
    def get_cupcake(flavor):
        print(f"Here is your {flavor} cupcake 🧁")
else:
    def get_cupcake(flavor):
        print(f"Here is your {flavor} cupcake 🧁")

print("Preparing...")
time.sleep(1)
get_cupcake("chocolate")