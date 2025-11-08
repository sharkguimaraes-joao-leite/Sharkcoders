#Variable Scope = Where a variable is visible and accesible
#Scope Resolution = (L.E.G.B) Local -> Enclosed -> Global -> Butt (Built-in)

#Local Scope = Variables that can't see outside of their function but can inside of their function

def num_1(num1):
    a = num1
    print(a)

def num_2(num2):
    b = num2
    print(b)

num_1(3)
num_2(8)
print("-----------------------------")

#Enclosed Scope = Variables in functions that contain other functions can see inside both functions

def num_3(num3):
    c = num3
    def function():
        print(c)
    function()

num_3(5)
print("-----------------------------")

#Global Scope = Value in and outside of functions that can interact with all functions containing it

def num_4():
    print(x)

def num_5():
    print(x)

x = 69

num_4()
num_5()
print("-----------------------------")

#Built-in Scope = Variable already in Python that the programer doesn't create
from math import e

def idk():
    print(f"{e:.3f}")

def tbh():
    print(f"{e:.3f}")

idk()
tbh()