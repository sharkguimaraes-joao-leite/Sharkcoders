#If statements: Execute some code only if a condition is true

#Example 1: Python Calculator

operation = input("Enter an operator (+ - * /): ")
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if operation == "+":
    add = (num_1) + (num_2)
    print(f"Your operation is equal to {round(add, 2)}.")
elif operation =="-":
    sub = (num_1) - (num_2)
    print(f"Your operation is equal to {round(sub, 2)}.")
elif operation =="*":
    mul = (num_1) * (num_2)
    print(f"Your operation is equal to {round(mul, 2)}.")
elif operation == "/":
    div = (num_1) / (num_2)
    print(f"Your operation is equal to {round(div, 2)}.")
else:
    print("You didn't pick a valid operator.")



#Exercise 1: Weight Converter

w = float(input("What is your weight?: "))
unit = input("Is your weight in Kilograms or Pounds (please type K or L): ").upper()

if unit == "K":
    w_l = w * 2.205
    print(f"Your weight in pounds is {w_l} Lbs, or, rounded, {round(w_l, 1)}Lbs.")
elif unit == "L":
    w_k = w / 2.205
    print(f"Your weight in kilograms is {w_k} K, or, rounded, {round(w_k, 1)}K.")
else:
    print("You didn't pick a valid unit.")



#Exercise 2: Temperature converter

unit = input("What is your temperature measuring unit (C or F)?: " ).upper()
temp = float(input("What is your temperature?: "))

if unit == "C" or "c":
    temp_f = temp * 1.8 + 32
    print(f"Your temperature in Fahrenheit is {temp_f}.")
elif unit == "F" or "f":
    temp_c = (temp - 32) / 1.8
    print(f"Your temperature in Celsius is {temp_c}.")
elif temp.isdigit() == False:
    print("You didn't pick a full number, asshole")
else:
    print("You didn't pick a valid unit.")