#For Loops = Execute a block of code a fixed number of times

for x in range(1, 11):
    print(x)


for x in reversed(range(1, 11)):
    print(x)
    
print("HAPPY NEW YEAR!")

#You can also use the step function to count in steps of 2, 3, etc...


for x in range(3, 13, 3):
    print(x)


#You can also itirate over a string

food = "Beans"

for x in food:
    print(x)


#Here are some other commands with useful functions both in for and while loops:

#Continue = Skip over a character in a sequence

for x in range (1, 16):
    if x == 7:
        continue
    else:
        print(x)

#Break = Stops a loop at a certain point

pizza = "Pepperoni"

for x in pizza:
    if x == "o":
        break
    else:
        print(x)