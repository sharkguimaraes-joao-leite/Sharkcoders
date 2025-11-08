#Functions = Blocks of reusable code. Usable by writing () after the function name.
#To define a function, we use the def command

def happy_bday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"They are {age} years old!")
    print("They look like crap,")
    print("And smell even worse")
    print()

happy_bday("John", 59)
happy_bday("Ana", 27)

#You can add variables in the def portion of the code and in other uses of the function replace them with values

def taxes(name, amount, due_date):
    print(f"Hello {name}.")
    print(f"You owe the IRS {amount:.2f}€.")
    print(f"You have to pay us until {due_date} or we will hire a hitman to kill you...")
    print("Have a nice day!")
    print()

taxes("Steve", 875.50, "July 5th")
taxes("Gabby", 489.99, "December 2nd")

#You can use the return statement to end a function and send the result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(6, 5))
print(subtract(4, 2))
print(multiply(5, 8))
print(divide(9, 3))

def create_name(frst, last):
    frst = frst.capitalize()
    last = last.capitalize()
    return frst + " " + last

full_name = create_name("joe", "schmoe")

print(full_name)