#if __name__ == '__main__' = Specific if statement with unique properties
#Can be run standalone or with another file if it is imported

def main():
    pass

if __name__ == '__main__':
    pass

#For more information about how this crap works, see scripts 1 and 2

from script_1 import *

if __name__ == '__main__':
    main()
print("-------------------------------------------")
from script_2 import *

if __name__ == '__main__':
    main()
print("-------------------------------------------")

#Exercise 1 = Python Slot Machine
import random
import time

def spin_row():
    symbols = ['🍎', '🍒', '🌸', '🍋', '🍌']
    return [random.choice(symbols) for x in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍎":
            return bet * 2
        elif row[0] == "🍒":
            return bet * 2.5
        elif row[0] == "🌸":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 3.5
        else:
            return bet * 5

def main():
    balance = 100.00
    payout = 0.00
    running = True
    print("****************************")
    print("Welcome to the PYTHON LOTTERY")
    print("Slots: 🍎 🍒 🌸 🍋 🍌")
    print("****************************")
    while running:
        while balance > 0:
            try:
                print(f"Currently, you have {balance:.2f}€!")
                print("-------------------------------------------")
                bet = float(input("How much do you wanna bet, friendo? "))
                print("-------------------------------------------")
                if bet > balance:
                    print(f"You only have {balance:.2f}€ my man, let's not go wild here!")
                    print("-------------------------------------------")
                elif bet == 0:
                    print("Ya can't bet nothin', buddy!")
                    print("-------------------------------------------")
                elif bet < 0:
                    print("What! Ya wantin' me to give ya money?!")
                    print("-------------------------------------------")
                elif bet >= balance / 2:
                    print("WOAH! That's a lotta money! I like ya!")
                    print("-------------------------------------------")
                    balance -= bet
                    break
                elif 0 < bet < 101:
                    print("Alright, thank ya so much!")
                    print("-------------------------------------------")
                    balance -= bet
                    break
            except ValueError:
                print("That ain't valid, my man!")
        row = spin_row()
        print("Spinning...")
        time.sleep(1)
        print_row(row)
        print("-----------------------------------------------")
        float(payout) == get_payout(row, bet)
        if payout == bet * 5:
            print("Ya won the jackpot! Be happy, you deserve it!")
        elif payout > 0:
            print("You won! Yippee, confetti, sparkles and unicorns!")
        else:
            print("You lost! Skill issue tbh")

        while True:
            play_again = input("Play again (y/n): ").lower()
            if play_again == "y":
                print("Okay :)")
                print("------------------------------------------")
                break
            elif play_again == "n":
                print("Goodbye!")
                balance = 0
                running = False
                break
            else:
                print("You can't write that :(")

if __name__ == '__main__':
    main()