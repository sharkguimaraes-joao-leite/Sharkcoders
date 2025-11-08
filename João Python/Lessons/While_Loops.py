#While Loops = Execute some code while other condition remains True

name = input("What is your name?: ")

while name == "":
    print("You didn't enter your name.")
    name = input("Re-enter your name?: ")
else:
    print(f"Hello {name}. Since when did you get so fat?")


age = int(input("How old are you?: "))

while age < 0:
    print("Your age cannot be negative")
    age = int(input("How old are you?: "))

while age > 130:
    print("You are too old to be alive!")
    age = int(input("How old are you?: "))

if age >= 0 and age < 18:
    print("Hello kid!")
else:
    print("Hello sir/ma'am.")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"So you like {food}, interesting...")
    food = input("Enter another food you like (q to quit): ")

print("Okay, goodbye!")


num = int(input("Enter a number between 1 and 10 without decimals: "))

while num < 1 or num > 10:
    print(f"{num} isn't an option, dumbass!")
    num = float(input("Enter a new number between 1 and 10: "))
else:
    print(f"You picked {num}")


#Exercise 1: Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Please enter a starting value in euros: "))
    if principle <= 0:
        print("The starting value can't be zero or less.")

while rate <=0:
    rate = float(input("Please enter an interest rate: "))
    if rate <= 0:
        print("The interest rate can't be zero or less.")

while time <=0:
    time = int(input("Please enter a time in years: "))
    if time <= 0:
        print("The time can't be zero or less years.")

amount = principle * pow((1 + rate/100), time)

print(f"After {time} year/s, your {principle}€ will become {amount:.2f}€!")