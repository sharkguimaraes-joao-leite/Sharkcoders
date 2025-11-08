 #Input = A function that promps the user to enter data
name = input("What is your name: ")
age = input("How old are you?: ")
age = int(age)
new_age = age + 1

#Print + Input functions
print(f"Hello {name}!")
print(f"You are {age} years old")
print(f"Next year, you will be {new_age} years old. How exciting!")
#User input is always a string, if you want it to be a number, it's best to typecast it as an integer or a float

#Exercise 1 Rectangle Area Calculator

width = float(input("What is the width of the rectangle in cm?: "))
length = float(input("What is the length of the rectangle in cm?: "))
area = width * length

print(f"The area of the rectangle is {area} cm squared")


#Exercise 2 Shopping Cart Program

item = str(input("What item would you like to buy?: "))
price = float(input("What is the price of the item?: "))
amount = int(input(f"How many {item}s would you like to buy?: "))
price_total = amount * price

print(f"The total price of your {item}/s will be €{price_total}")


#Exercise 3: Random Story Game

print("Today I went to a zoo in...")
zoo_location = input("Where was the zoo?: ")
print(f"Today I went to a zoo in {zoo_location}.")
print(f"I love {zoo_location} because it is very...")
adjective1 = input(f"Write an adjective that {zoo_location} is: ")
print(f"I love {zoo_location} because it it very {adjective1}!")


#Exercise 4: Validate User Input

old_name = input("What would you like to be your username?: ")

length = len(old_name)
space = old_name.count(" ")
alp = old_name.isalpha()
old_name = old_name.capitalize()

if length > 12:
    print("Please write an username with less than 13 characters")
elif space >= 1:
    print("Please write an username without any spaces")
elif alp == False:
    print("Please write an username without any special characters or digits")
else:
    print(f"Hello {old_name}, nice to meet you!")