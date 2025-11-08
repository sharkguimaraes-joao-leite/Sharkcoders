 #Dictionary = A collection of "key" - "value" pairs separated by colons. 
#Ordered and changeable but cannot contain duplicates

capitals = {"Portugal": "Lisbon",
            "Japan": "Tokyo",
            "France": "Paris",
            "England": "London"}

#To get the value of a key, you use the get command. If the dictionary doesn't contain the key, it will return "None".

print(capitals.get("Portugal"))

#You can combine dictionaries with if statements much like how you would use booleans (True or False)

if capitals.get("France"):
    print("That capital is on the list")
else:
    print("That capital isn't on the list")

#You can also add or change a value in a dictionary with the update command

capitals.update({"China": "Beijing"})
capitals.update({"Japan": "Oslo"})

print(capitals)

#You can remove a key:value pair in a dictionary by using the pop command with a key value
#If you don't put a key value and use popitem(), it will delete the latest added key:value in a dictionary

capitals.pop("Japan")

print(capitals)

#To get all the keys or all the values in a dictionary, you use the key and value commands

print(capitals.keys())

print(capitals.values())

#You can itirate over the previous commands with a for loop

for key in capitals.keys():
    print(key)

print("-----------------------------------------------------------")

for value in capitals.values():
    print(value)

#You can use the items command to print a dictionary that resembles a 2D list and is iterable with a for loop
capitals.items()


for key, value in capitals.items():
    print(f"{key}, {value}")

 #If you try to iterate over a dictionary, it will only register the keys and not the values


 #To clear a dictionary, you use the clear command

capitals.clear()


#Exercise 1: Concession Stand Program

items =  {"popcorn": 2.99,
          "soda": 1.99,
          "popsicle": 2.50,
          "fresh water": 0.99,
          "pretzel": 2.99}

ticket = []
total = 0

print("------------MENU------------")

for key, value in items.items():
    print(f"The {key} costs {value}€.")

print("----------------------------")

while True:
    food = input("Please select a food item (q to quit): ").lower()
    if food == "q":
        print("Okay!")
        break
    elif items.get(food) is None:
        print("That item is not on our menu! Sneaky bastard...")
    else:
        ticket.append(food)

print("-----------ORDER------------")
for food in ticket:
    total = total + items.get(food)
    print(food, end = " ")

print()
print(f"Your total is {total:.2f}€")