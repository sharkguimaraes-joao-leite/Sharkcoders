#Collections = Single variables used to store multiple values
#You can iterate over collections with the for loop

#  List  = [] Ordered and changeable. Can contain duplicates.

vegetables = ["Lettuce", "Zuchinni", "Carrot", "Potato", "Eggplant"]

print(vegetables[0:2])


for vegetable in vegetables:
    print(vegetable)


#You can use the length function to count how many values are in a list if you're stupid and don't know how to count

print(len(vegetables))


#You can use the in function to create a boolean that will tell you if a value is in a list

veg = "Eggplant"

if veg in vegetables:
    print(f"{veg} is in the list of vegetables")
else:
    print(f"{veg} is not in the list of vegetables")

#You can add, remove, change, reorder, clear or count the number of values in a list

vegetables[0] = "Onion"

print(vegetables)


vegetables.append("Celery")

for vegetable in vegetables:
    print(vegetable)


vegetables.remove("Zuchinni")

print(vegetables)


vegetables.insert(3, "Turnip")

for vegetable in vegetables:
    print(vegetable)


vegetables.sort()

print(vegetables)


vegetables.reverse()

for vegetable in vegetables:
    print(vegetable)


print(vegetables.index("Carrot"))


vegetables.insert(1, "Eggplant")
print(vegetables.count("Eggplant"))


vegetables.pop()
print(vegetables)


vegetables.clear()

print(vegetables)


#  Set = {} Unordered and immutable. You can add and remove values, but there cannot be duplicates.

fruits = {"Orange", "Strawberry", "Pineapple", "Apple"}
print(fruits)

#Some commands of lists can also work with sets, such as length, in, add, remove and clear


#Tuple = () Ordered and unchangeable. Can contain duplicates. Are faster than lists.

meals = ("Spaghetti", "Pizza", "Lasagna", "Sandwich", "Sushi")

#The only functions with tuples are count, index, length and in.

#Exercise 1 = Shopping cart program

buying = True

foods = []
prices = []
total = 0

while buying == True:
    food = input("What food would you like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"What is the price of a {food} in €?: "))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for x in foods:
    print(x)

for price in prices:
    total += price

print()
print(f"Your total is {round(total, 2)}€ ")


#2D Lists = A list composed of other lists

gaming = ["Nintendo", "Sega", "Sony", "Xbox"]
cars =   ["Citroen", "Hyundai", "Peugeot", "Audi"]
movies = ["Disney", "Dreamworks", "Pixar", "Marvel"]

brands = [gaming, cars, movies]

for x in brands:
    print(x)

#You can use the index function to find a 1D list in a 2D list

print()
print(brands[0])
print()
print(brands[2])
print()
print(brands[1])

#You can use a double index to find a value in a 1D list inside a 2D list (wow that was a mouthful)

print()
print(brands[1][2])

#To iterate over a value in a 2D list, you have to use nested loops

for gaming in brands:
    for game in gaming:
        print(game, end=" ")
    print()

#You can also make a 2D list out of tuples, but you won't be able to change the values


#Exercise 2 = Python quiz

questions = ("What year was the battle of S. Mamede?: ",
             "What year was The Legend of Zelda released?: ",
             "How many atoms exist in a molecule of water?: ",
             "What are the first 5 digits of pi?: ",
             "How many seconds does an hour have?: ")

options = (("1179", "1128", "1106", "1147"),
           ("1999", "1981", "1986", "1975"),
           ("1", "2", "3", "4"),
           ("3.1415", "2.1675", "3.4561", "4.6713"),
           ("60", "600", "360", "3600"))

answers = ("1128", "1986", "3", "3.1415", "3600")
guesses = []
score = 0
ques_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter an answer: ")
    guesses.append(guess)
    if guess == answers[ques_num]:
        print("You are correct! You got 100 points!")
        score += 100
    else:
        print(f"Wrong, you moron, the right answer was {answers[ques_num]}!")
    
    
    ques_num += 1
print("----------------------------")

ans = score / 100
ans = int(ans)

if score > 0:
   print(f"Congratulations! Your score is {score}!")
   print(f"You got {ans} answers correct!")
else:
    print("WOW, you got 0 points?! Talk about embarrassing!")