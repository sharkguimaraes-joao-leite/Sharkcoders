 #Arithmetic & Math

friends = 6
#friends += 1
#friends -= 2
#friends *= 4
#friends /= 2
#friends **= 2 (exponent)
#remainder = friends % 4 (remainder of a division)

print(f"You have {friends} friends")

#If you would like to see different operations, remove the # from the operations above


#Math Related Functions Already Built In On Python

w = 5
x = 5.7
y = 2.5
z = -8

result1 = round(x)
print(result1)

result2 = abs(z)
print(result2)

result3 = pow(y, 3)
print(result3)

result4 = max(w, x, y, z)
print(result4)

result5 = min(w, x, y, z)
print(result5)

#Functions with the "Import Math" function
import math

print(math.pi)

print(math.e)

result6 = math.sqrt(w)
print(result6)

result7 = math.ceil(y)
print(result7)

result8 = math.floor(x)
print(result8)


#Exercise 1: Circunference & Area of a Circle

r = float(input("What is the radius of the circle in cm?: "))

cir = 2 * math.pi * r
rnd_cir = round(cir)

area = math.pi * pow(r, 2)
rnd_area = round(area, 2)

print(f"The circunference of your circle is {cir} cm, or, rounded, {rnd_cir} cm.")
print(f"The area of your circle is {area} cm^2, or, rounded, {rnd_area} cm^2")


#Exercise 2: Hipotenuse of a rectangle

a = float(input("What is the length of your rectangle in cm: "))
b = float(input("What is the width of your rectangle in cm: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
c_rnd = round(c)

print(f"The hipotenuse of your rectangle is {c}, or, rounded, {c_rnd}.")
#Don't forget that, when asking for user input, set to an integer or float in math 


#Exercise 3 = BMI Calculator
print("-----------------------------------------------------------")

while True:
    weight = input("How much do you weight in kilograms rounded down: ")
    print("-----------------------------------------------------------")

    if weight.isdigit():
        weight = float(weight)
        break
    else:
        print("That value isn't valid, pick again")
        print("--------------------------------------------------------------")

while True:
    height = input("How much do you weight in centimeters rounded down: ")
    print("-----------------------------------------------------------")

    if height.isdigit():
        height = float(height)
        break
    else:
        print("That value isn't valid, pick again")
        print("--------------------------------------------------------------")

height /= 100

bmi = weight / (height * height)

print(f"Your BMI is equal to {bmi:.1f}")