#Randomness = LET'S GO GAMBLING!!!1!!1!1!11 (with the import random module)

import random

#If you type random.rand and type int after, it will generate a random value based on the range of said integer
#You can also substitute the values with other variables

dnd = random.randint(1, 20)

print(dnd)
 
print("-------------------------------------------------------")

unlucky = 1

lucky = 100

print(random.randint(unlucky, lucky))

#If you want a random value between 0 and 1, you can type random.random()

print("-------------------------------------------------------")

print(random.random())


#You can use collections as the values to print a random value inside a collection with the choice command

print("-------------------------------------------------------")

gun = ("Rock", "Paper", "Scissors")

print(random.choice(gun))

#You can use the shuffle command to randomlly sort the values in a collection

print("-------------------------------------------------------")

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_order = random.shuffle(deck)

for card in deck:
    print(card)
 

#Exercise 1 = Random Number Guessing Game

print("-------------------------------------------------------")

bot = random.randint(1, 10)

while True:
    person = input("Pick a full number between 1 and 10: ")
    if person.isdigit() == False:
        print("That value isn't valid, pick again!")
        print("-----------------------------------------------------------")
    else:
        person = int(person)
        if person <= 0:
            print("That number is too small, pick again!")
            print("-------------------------------------------------------")
        elif person >= 11:
            print("That number is too big, pick again!")
            print("-------------------------------------------------------")
        else:
            break

print("-------------------------------------------------------")

if bot == person:
    print("Aww shucks, you beat me! Well, see ya next time!")
else:
    print(f"Oof, sorry, my number was {bot}. You were close though...")


#Exercise 2 = Rock Paper Scissors Game

print("-------------------------------------------------------")

nuclear_bomb = ("rock", "paper", "scissors")

clanker = random.choice(nuclear_bomb)

while True:
    person = input("Please choose rock, paper or scissors: ").lower()
    if person not in nuclear_bomb:
        print(f"{person} isn't valid, pick again!")
        print("---------------------------------------------------------")
    else:
        break

if person == clanker:
    print(F"Looks like we both picked {person}!")
elif person == "scissors" and clanker == "paper":
    print(f"You beat me, I picked paper! Well played") 
elif person == "paper" and clanker == "rock":
    print("You beat me, I picked rock! Well played!")
elif person == "rock" and clanker == "scissors":
    print(f"You beat me, I picked scissors! Well played") 
else:
    print(f"I picked {clanker} and you picked {person}. I WON!!!!")
