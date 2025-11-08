#Python Program to exercise mental calculus
import random

#Variables
mathing = True
operators = ("+", "-", "*", "/")
points = 0
asking = True
multiplier = 1.0

#Main Code
while mathing:
    asking = True
    points = 0
    while True:
        try:
            count = int(input("How many operations do you want to solve?: "))
            print("------------------------------------------------------")
            if count > 0:
                break
            else:
                print("You can't solve 0 or less operations!") 
                print("------------------------------------------------------")
        except ValueError:
            print("Write a number!")
            print("------------------------------------------------------")
    for x in range(1, count + 1):
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100) 
        operator = random.choice(operators)
        if operator == "+":
            result = num_1 + num_2
            while True:
                try:
                    guess = int(input(f"{num_1} + {num_2} = "))
                    print("------------------------------------------------------")
                    if guess == result:
                        print("Correct!")
                        print("------------------------------------------------------")
                        points += 100
                        break
                    else:
                        print("Wrong!")
                        print("------------------------------------------------------")
                        break
                except ValueError:
                    print("Write a number!")
                    print("------------------------------------------------------")
        elif operator == "-":
            result = num_1 - num_2
            while True:
                try:
                    guess = int(input(f"{num_1} - {num_2} = "))
                    print("------------------------------------------------------")
                    if guess == result:
                        print("Correct!")
                        print("------------------------------------------------------")
                        points += 100
                        break
                    else:
                        print("Wrong!")
                        print("------------------------------------------------------")
                        break
                except ValueError:
                    print("Write a number!")
                    print("------------------------------------------------------")
        elif operator == "*":
            result = num_1 * num_2
            while True:
                try:
                    guess = int(input(f"{num_1} * {num_2} = "))
                    print("------------------------------------------------------")
                    if guess == result:
                        print("Correct!")
                        print("------------------------------------------------------")
                        points += 100
                        break
                    else:
                        print("Wrong!")
                        print("------------------------------------------------------")
                        break
                except ValueError:
                    print("Write a number!")
                    print("------------------------------------------------------")
        else:
            result = num_1 / num_2
            while True:
                try:
                    guess = float(input(f"{num_1} / {num_2} = "))
                    print("------------------------------------------------------")
                    if round(result) == round(guess):
                        print("Correct!")
                        print("------------------------------------------------------")
                        points += 100
                        break
                    else:
                        print("Wrong!")
                        print("------------------------------------------------------")
                        break
                except ValueError:
                    print("Write a number!")
                    print("------------------------------------------------------")
    print(f"You got {points} points!")
    print("------------------------------------------------------")
    while asking:
        again = input("Play again (y/n)?: ").lower()
        print("------------------------------------------------------")
        if again == "y":
            print("OK!")
            print("------------------------------------------------------")
            asking = False
            break
        elif again == "n":
            print("Bye...")
            mathing = False
            asking = False
            break
        else:
            print("Write y or n")
            print("------------------------------------------------------")