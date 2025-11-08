#*args = Arbitrary arguments that allow you to pass multiple non-key arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

add(3, 5, 6, 4)

#You can use other names when using the *args and **kwargs function, as long as you keep the unpacking operator (*).
print("-------------------------------------------")

def display_name(*names):
    for name in names:
        print(name, end = " ")

display_name("Mr.", "Joe", "Gabriel", "Schmoe", "II")
print()

#**kwargs = Arbitrary arguments that allow you to pass multiple keyword arguments
print("--------------------------------------------")

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(Street = "Floor St.",
        City = "Los Angeles",
        State = "California")

print("--------------------------------------------")


#Exercise 1 = Combining Regular Arguments with Key-Word Arguments

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    if "apt" in kwargs:
       print(f"{kwargs.get('street')} {kwargs.get('apt')}")
       kwargs.pop("street")
       kwargs.pop("apt")
    else:
        print(f"{kwargs.get('street')}")
        kwargs.pop("street")
    for value in kwargs.values():
        print(value, end = " ")

shipping_label("Dr.", "Steve", "IV",
               street = "Wall Street",
               apt = "#167",
               city = "New York",
               country = "USA")